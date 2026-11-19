"""Exit Forge Shell."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult


class ExitCommand(BaseCommand):
    name = "exit"
    category = "system"
    description = "Exit MiniOS Shell"
    syntax = "exit"
    examples = ("exit",)

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        return CommandResult(output="Goodbye from MiniOS.", should_exit=True)
