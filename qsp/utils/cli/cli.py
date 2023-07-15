from rich.console import Console
from rich.panel import Panel
from typer import Context, Exit, Option, Typer

from qsp import __version__

console = Console()


def version_func(flag):
    if flag:
        console.print(
            Panel(
                f"[grey82]qsp@{__version__}[/grey82]",
                style="blue",
                title="Version",
                title_align="left",
            )
        )
        raise Exit(code=0)


def callback(
    ctx: Context,
    version: bool = Option(
        False,
        callback=version_func,
        is_flag=True,
    ),
):
    message = "[yellow1]Usage[/yellow1]: qsp [FRAMEWORK] [TEMPLATE] [OPTIONS]\nTry: 'qsp --help' for help\n" # noqa
    console.print(message)


def add_version_callback(app: Typer):
    app.callback(invoke_without_command=True)(callback)
