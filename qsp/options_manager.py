import yaml


class OptionsManager:
    def __init__(self, file, parameters) -> None:
        self.file = file
        if file:
            with open(file, "r") as file:
                yaml_data = yaml.safe_load(file)
                self.variables = {**parameters, **yaml_data}
        else:
            self.variables = parameters

    def __str__(self) -> str:
        return self.file
