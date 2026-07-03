"""Discover and load community applications from the Apps/ folder."""

from __future__ import annotations

import importlib.util
import inspect
import json
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell.commands.base import BaseCommand
    from shell.registry import CommandRegistry

_INSTALLED: list["CommunityApp"] = []


@dataclass(frozen=True)
class CommunityApp:
    """Metadata for a community app in Apps/."""

    folder: str
    name: str
    command: str
    description: str
    author: str
    version: str
    website: str = ""


def apps_directory() -> Path:
    """Return the path to the community Apps folder at the repo root."""
    return Path(__file__).resolve().parent.parent / "Apps"


def installed_apps() -> list[CommunityApp]:
    """Return community apps loaded during the current session."""
    return list(_INSTALLED)


def load_community_apps(registry: CommandRegistry) -> list[CommunityApp]:
    """Scan Apps/, register commands, and return loaded app metadata."""
    global _INSTALLED
    _INSTALLED = []

    apps_dir = apps_directory()
    if not apps_dir.is_dir():
        return _INSTALLED

    from shell.commands.base import BaseCommand

    for entry in sorted(apps_dir.iterdir()):
        if not entry.is_dir() or entry.name.startswith((".", "_")):
            continue

        manifest_path = entry / "app.json"
        command_path = entry / "command.py"
        if not manifest_path.is_file() or not command_path.is_file():
            continue

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue

        command_name = str(manifest.get("command", "")).strip()
        if not command_name:
            continue

        if registry.has(command_name):
            continue

        module_name = f"forgeos_community_app_{entry.name}"
        spec = importlib.util.spec_from_file_location(module_name, command_path)
        if spec is None or spec.loader is None:
            continue

        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception:
            continue

        command_class: type[BaseCommand] | None = None
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if (
                issubclass(obj, BaseCommand)
                and obj is not BaseCommand
                and getattr(obj, "name", "")
            ):
                command_class = obj
                break

        if command_class is None:
            continue

        registry.register(command_class)
        app = CommunityApp(
            folder=entry.name,
            name=str(manifest.get("name", entry.name)),
            command=command_name,
            description=str(manifest.get("description", command_class.description)),
            author=str(manifest.get("author", "Community")),
            version=str(manifest.get("version", "1.0.0")),
            website=str(manifest.get("website", "")),
        )
        _INSTALLED.append(app)

    return _INSTALLED
