# from rich import inspect
from os import path

from qsp.utils.cli import FileArgument, OutputArgument, ParamsManager
from qsp.utils.cli import TypeOption as Option
from qsp.utils.runner import Workflow
from rich.console import Console
from typer import Typer

from .categories import Categories
from .validator import DjangoParamsValidator

django = Typer()
console = Console()


@django.command()
def restapi(
    output: str = OutputArgument(),
    template: str = FileArgument(),
    docker: Option("docker compose", Categories.DEVOPS) = False,
    dockerfile: Option("dockerfile", Categories.DEVOPS) = False,
    # fmt: off
    github_worflow4ec2: Option("github workflow EC2 instance via ssh", Categories.DEVOPS) = False,
    # fmt: on
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
    # Merge file variables with params
    vmanager = ParamsManager(template, locals())

    # Validate params
    DjangoParamsValidator(vmanager.variables)

    # Get workflow path
    intern_path = path.dirname(path.abspath(__file__))
    workflow_path = path.join(intern_path, "workflows/restapi.yml")

    # Run workflow
    workflow = Workflow(workflow_path)
    workflow.run(vmanager.variables)
