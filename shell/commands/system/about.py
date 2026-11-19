
"""Display information about MiniOS."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult
from shell.ui.panels import ForgePanel


class AboutCommand(BaseCommand):
    name = "about"
    category = "system"
    description = "Display information about MiniOS"
    syntax = "about"
    examples = ("about",)

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        panel = ForgePanel(
            "[bold cyan]MiniOS[/bold cyan] is a Python-based operating system simulator.\n\n"
            "It provides a command-line environment with user management,\n"
            "a virtual filesystem, package management, and system utilities.\n\n"
            "MiniOS simulates operating system features. It is not a real\n"
            "bootable operating system or hardware-level kernel.",
            title="About MiniOS",
            border_style="cyan",
        )
        return CommandResult(renderable=panel.render())
