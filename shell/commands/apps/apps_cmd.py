"""List and run community applications from the Apps/ folder."""

from typing import Any

from shell.commands.base import BaseCommand, CommandResult
from shell.community_apps import apps_directory, installed_apps
from shell.ui.tables import ForgeTable


class AppsCommand(BaseCommand):
    name = "apps"
    category = "apps"
    description = "List community applications from the Apps/ folder"
    syntax = "apps [COMMAND]"
    examples = ("apps", "apps hello", "apps info hello")

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        community = installed_apps()
        builtin = [
            cls
            for cls in context["registry"].all_commands()
            if cls.category == "apps" and cls.name != "apps"
        ]

        if not args:
            return self._list_apps(community, builtin)

        subcommand = args[0].lower()
        if subcommand in ("info", "show") and len(args) > 1:
            return self._show_info(args[1], community)

        target = args[0]
        registry = context["registry"]
        if registry.has(target):
            from shell.dispatcher import CommandDispatcher

            dispatcher: CommandDispatcher = context["dispatcher"]
            session = context["session"]
            from shell.parser import CommandParser

            parser: CommandParser = context["parser"]
            parse_result = parser.parse(target + (" " + " ".join(args[1:]) if len(args) > 1 else ""))
            if not parse_result.commands:
                return CommandResult(output=f"apps: could not run '{target}'", exit_code=1)
            result = dispatcher.dispatch_single(parse_result.commands[0], session)
            return CommandResult(
                output=result.output,
                renderable=result.renderable,
                exit_code=result.exit_code,
                should_exit=result.should_exit,
                clear_screen=result.clear_screen,
            )

        return CommandResult(
            output=(
                f"apps: unknown application '{target}'. "
                f"Run 'apps' to see installed apps, or add one in {apps_directory()}"
            ),
            exit_code=1,
        )

    def _list_apps(
        self,
        community: list,
        builtin: list,
    ) -> CommandResult:
        table = ForgeTable(title="Forge OS Applications")
        table.add_column("Command", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Description")
        table.add_column("Source", style="magenta")

        for app in community:
            table.add_row(app.command, app.name, app.description, f"Apps/{app.folder}")

        for command_class in sorted(builtin, key=lambda cls: cls.name):
            table.add_row(command_class.name, command_class.name, command_class.description, "built-in")

        if not community and not builtin:
            return CommandResult(
                output=(
                    "No applications installed yet.\n"
                    f"Add one by creating a folder in: {apps_directory()}\n"
                    "See CONTRIBUTIONS.md for the full guide."
                )
            )

        return CommandResult(renderable=table.render())

    def _show_info(self, command_name: str, community: list) -> CommandResult:
        for app in community:
            if app.command == command_name:
                lines = [
                    f"[bold cyan]{app.name}[/bold cyan] ({app.command})",
                    "",
                    f"[bold]Description:[/bold] {app.description}",
                    f"[bold]Author:[/bold] {app.author}",
                    f"[bold]Version:[/bold] {app.version}",
                    f"[bold]Folder:[/bold] Apps/{app.folder}",
                ]
                if app.website:
                    lines.append(f"[bold]Website:[/bold] {app.website}")
                lines.append("")
                lines.append(f"Run with: [cyan]{app.command}[/cyan]")
                return CommandResult(output="\n".join(lines))

        return CommandResult(output=f"apps: no community app named '{command_name}'", exit_code=1)
