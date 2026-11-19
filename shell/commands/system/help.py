
"""Display available MiniOS commands or help for a command."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult
from shell.ui.tables import ForgeTable


class HelpCommand(BaseCommand):
    name = "help"
    category = "system"
    description = "Display available MiniOS commands"
    syntax = "help [COMMAND]"
    examples = (
        "help",
        "help ls",
    )

    VISIBLE_COMMANDS = {
        "help", "clear", "about", "uname", "free",
        "ps", "users", "reboot", "shutdown", "version",
        "ls", "cd", "pwd", "mkdir", "touch", "cat", "rm",
        "whoami", "passwd", "logout", "date", "time", "echo",
        "hostname", "uptime", "calc", "history", "tree", "find", 
        "wc", "head", "tail",
    }

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        registry = context["registry"]

        if args:
            command_class = registry.get(args[0])
            if command_class is None or command_class.name not in self.VISIBLE_COMMANDS:
                return CommandResult(
                    output=f"help: no help entry for '{args[0]}'",
                    exit_code=1,
                )
            return CommandResult(output=command_class().help_text())

        table = ForgeTable(title="MiniOS Commands")
        table.add_column("Command", style="cyan")
        table.add_column("Category", style="magenta")
        table.add_column("Description")

        for category, commands in registry.by_category().items():
            for command_class in commands:
                if command_class.name in self.VISIBLE_COMMANDS:
                    table.add_row(
                        command_class.name,
                        category,
                        command_class.description,
                    )

        return CommandResult(renderable=table.render())
