from qsp.utils.validators import ParamsValidator
from qsp.utils.validators.rules import JustOneOfThese, Need


class DjangoParamsValidator(ParamsValidator):
    def __init__(self, vmanager: dict) -> None:
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
