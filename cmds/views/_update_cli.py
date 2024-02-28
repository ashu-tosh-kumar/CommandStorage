from datetime import datetime
from pathlib import Path
from typing import Annotated

import typer

from cmds.controller.cmds import get_cmds
from cmds.models.enums import arguments as arguments_enums
from cmds.models.enums import error as error_enums
from cmds.views.cli import app

DEFAULT_FILE_LOCATION = Path().joinpath(f"command_storage_export_{datetime.now()}.json")

_INITIAL_NEW_KEY = typer.Option(
    None,
    arguments_enums.Arguments.KEY.value.long,
    arguments_enums.Arguments.KEY.value.short,
    help=arguments_enums.Arguments.KEY.value.description,
)
_INITIAL_COMMAND = typer.Option(
    None,
    arguments_enums.Arguments.COMMAND.value.long,
    arguments_enums.Arguments.COMMAND.value.short,
    help=arguments_enums.Arguments.COMMAND.value.description,
)
_INITIAL_DESCRIPTION = typer.Option(
    None,
    arguments_enums.Arguments.DESCRIPTION.value.long,
    arguments_enums.Arguments.DESCRIPTION.value.short,
    help=arguments_enums.Arguments.DESCRIPTION.value.description,
)


@app.command()
def update(
    orig_key: Annotated[str, typer.Argument(...)], new_key: str = _INITIAL_NEW_KEY, command: str = _INITIAL_COMMAND, description: str = _INITIAL_DESCRIPTION
) -> None:
    """Allows updating a stored command by its key. Also supports changing the key."""
    cmds = get_cmds()

    update_error = cmds.update(orig_key, new_key, command, description)

    if update_error == error_enums.Error.SUCCESS:
        typer.secho(
            f"Successfully updated command with key '{orig_key}': '{update_error}'",
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"Error in updating command with key '{orig_key}': '{update_error}'",
            fg=typer.colors.RED,
        )
