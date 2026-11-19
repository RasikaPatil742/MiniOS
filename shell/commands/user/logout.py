"""Log out of Forge Shell."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult


class LogoutCommand(BaseCommand):
    name = "logout"
    category = "user"
    description = "Log out and exit MiniOS Shell"
    syntax = "logout"
    examples = ("logout",)

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        user = context["users"].whoami()
        return CommandResult(
            output=f"Logged out {user}. Goodbye from MiniOS.",
            should_exit=True,
        )
