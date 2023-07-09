import yaml


class Workflow:
    def __init__(self, workflow: str) -> None:
        with open(workflow, "r") as file:
            data = yaml.safe_load(file)
        print(data)

    def run(self, vmanager: dict):
        ...
