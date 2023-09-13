import yaml
from rich import print as print_color

from qsp.utils import Loader

from .actions import Actions, Sections


class Workflow:
    def __init__(self, workflow_path: str, sections: Sections = Sections) -> None:
        self.sections = sections
        with open(workflow_path, "r") as file:
            self.workflow = yaml.safe_load(file)

    def run(self, vmanager: dict):
        actor = Actions(vmanager, self.sections)
        for index, step in enumerate(self.workflow[self.sections.steps]):
            with Loader(
                f"{str(index + 1)}. " + step[self.sections.step_name].title(),
                end=f"{str(index + 1)}. {step[Sections.step_name]}".title()
                + " [green]OK[/green]",
            ):
                actor.develop(step)
        print_color(
            f"\n[green]{self.workflow[self.sections.workflow_name].title()} Started Successfully![/green]"  # noqa
        )
