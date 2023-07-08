from typing import Any

from typer import Argument, Option
from typing_extensions import Annotated


def FileArgument(help="You can use a YML file to load settings", show_default=False):
    return Argument(None, help=help, show_default=show_default)


def TypeOption(
    help: str,
    category: str,
    help_start_with_include: bool = True,
    auto_title_texts: bool = True,
    type: Any = bool,
):
    if auto_title_texts:
        help = help.title()

    return Annotated[
        type,
        Option(
            help=help if not help_start_with_include else "Include " + help,
            rich_help_panel=category,
            show_default=False,
        ),
    ]
