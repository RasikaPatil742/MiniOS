"""Shut down MiniOS."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult


class ShutdownCommand(BaseCommand):
    name = "shutdown"
    category = "system"
    description = "Shut down MiniOS"
    syntax = "shutdown"
    examples = ("shutdown",)

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        return CommandResult(
            output="MiniOS is shutting down... Goodbye.",
            should_exit=True,
        )
