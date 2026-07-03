"""Hello — sample community app shipped with Forge OS."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult
from shell.ui.panels import ForgePanel


class HelloCommand(BaseCommand):
    name = "hello"
    category = "apps"
    description = "Greet the Forge OS community"
    syntax = "hello [NAME]"
    examples = ("hello", "hello developer")

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        name = " ".join(args) if args else context["session"].username or "friend"
        message = (
            f"Hello, {name}!\n\n"
            "This app was loaded from the Apps/ folder.\n"
            "Want to build your own? See CONTRIBUTIONS.md on GitHub."
        )
        panel = ForgePanel(message, title="Hello", border_style="cyan")
        return CommandResult(renderable=panel.render())
