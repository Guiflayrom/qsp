# from rich import inspect
from rich.console import Console
from typer import Typer

from qsp.options_manager import OptionsManager
from qsp.project_configuration import FileArgument
from qsp.project_configuration import TypeOption as Option

from .categories import Categories

django = Typer()
console = Console()
var_name = f"{django=}".partition("=")[0]


@django.command()
def restapi(
    file: str = FileArgument(),
    docker: Option("docker compose", Categories.DEVOPS) = False,
    dockerfile: Option("dockerfile", Categories.DEVOPS) = False,
    github_worflow4ec2: Option("github workflow EC2 instance via ssh", Categories.DEVOPS) = False,
    black: Option("black", Categories.LINTER) = False,
    blue: Option("blue", Categories.LINTER) = False,
    flake8: Option("flake8", Categories.LINTER) = False,
    separated_apps: Option("folder for apps", Categories.ORGANIZATION) = False,
    split_settings: Option("split settings", Categories.ORGANIZATION) = False,
    user_model: Option("default user model", Categories.MODEL_TEMPLATE) = False,
    jwt_model: Option("simple jwt configurations", Categories.APP) = False,
    cors: Option("cors headers configurations", Categories.APP) = False,
    logging: Option("logging configurations", Categories.APP) = False,
    makefile: Option("makefile", Categories.UTILS) = False,
    swagger: Option("swagger", Categories.UTILS) = False,
    gitignore: Option("gitignore", Categories.UTILS) = False,
    license: Option("license sets", Categories.UTILS) = False,
    poetry: Option("poetry", Categories.MANAGER) = False,
    pipenv: Option("pipenv", Categories.MANAGER) = False,
    redis: Option("redis", Categories.DATABASE) = False,
    postgresql: Option("postgresql", Categories.DATABASE) = False,
    mysql: Option("mysql", Categories.DATABASE) = False,
    sqlite: Option("sqlite", Categories.DATABASE) = False,
    uvicorn: Option("uvicorn", Categories.ASGI) = False,
    hypercorn: Option("hypercorn", Categories.ASGI) = False,
    daphne: Option("daphne", Categories.ASGI) = False,
    gunicorn: Option("gunicorn", Categories.WSGI) = False,
    uwsgi: Option("uwsgi", Categories.WSGI) = False,
    cherrypy: Option("cherrypy", Categories.WSGI) = False,
    waitress: Option("waitress", Categories.WSGI) = False,
):
    manager = OptionsManager(file, locals())
    console.log(manager.variables)
