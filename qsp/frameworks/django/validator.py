from qsp.utils.validators import ParamsValidator
from qsp.utils.validators.rules import JustOneOfThese, Need


class DjangoParamsValidator(ParamsValidator):
    def __init__(self, vmanager) -> None:
        self.vmanager = vmanager
        super().__init__(self.vmanager)

        self.add_rules(
            Need("docker", "dockerfile"),
            JustOneOfThese("black", "blue"),
            JustOneOfThese("postgresql", "sqlite", "mysql"),
            JustOneOfThese(
                "uvicorn",
                "hypercorn",
                "daphne",
                "gunicorn",
                "uwsgi",
                "cherrypy",
                "waitress",
            ),
        )


if __name__ == "__main__":
    DjangoParamsValidator(
        {
            "file": None,
            "docker": True,
            "dockerfile": True,
            "github_worflow4ec2": False,
            "black": True,
            "blue": False,
            "flake8": False,
            "separated_apps": False,
            "split_settings": False,
            "user_model": False,
            "jwt_model": False,
            "cors": False,
            "logging": False,
            "makefile": False,
            "swagger": False,
            "gitignore": False,
            "license": False,
            "poetry": False,
            "pipenv": False,
            "redis": False,
            "postgresql": False,
            "mysql": False,
            "sqlite": False,
            "uvicorn": False,
            "hypercorn": False,
            "daphne": False,
            "gunicorn": False,
            "uwsgi": False,
            "cherrypy": False,
            "waitress": False,
        }
    )
