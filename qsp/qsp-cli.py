from rich.console import Console
from typer import Exit, Typer

from qsp import __version__
from qsp.frameworks import TYPERS

console = Console()
app = Typer()


# Version
def version_func(flag):
    if flag:
        console.print(__version__)
        raise Exit(code=0)


# Add Typers
for FRAMEOWORK_TYPER in TYPERS:
    app.add_typer(FRAMEOWORK_TYPER["typer"], name=FRAMEOWORK_TYPER["name"])


if "__main__" == __name__:
    app()
