import yaml


class ParamsManager:
    def __init__(self, file, parameters) -> None:
        self.file = file
        if file:
            with open(file, "r") as file:
                yaml_data = yaml.safe_load(file)
                self.variables = {**parameters, **yaml_data}
        else:
            self.variables = parameters

    def __getitem__(self, key):
        if key in self.variables:
            return self.variables[key]

    def __str__(self) -> str:
        return str(self.variables)
