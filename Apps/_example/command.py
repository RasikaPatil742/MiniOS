"""Example community app — copy this folder to Apps/your-app-name/ and edit."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult


class MyAppCommand(BaseCommand):
    name = "myapp"
    category = "apps"
    description = "Short description of what your app does"
    syntax = "myapp [ARGS]"
    examples = ("myapp", "myapp world")

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        target = " ".join(args) if args else "Forge OS"
        return CommandResult(output=f"Hello from My App, {target}!")
