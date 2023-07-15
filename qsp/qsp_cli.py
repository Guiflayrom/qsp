from typer import Typer

from qsp.utils.cli import add_version_callback
from qsp.workflows import commands_subcommands

app = Typer()

# Version
add_version_callback(app)

# Add Typers
for tinstance, tcommand in commands_subcommands():
    app.add_typer(typer_instance=tinstance, name=tcommand)


if "__main__" == __name__:
    app()
