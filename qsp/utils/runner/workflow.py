import subprocess

import yaml
from jinja2 import Template

from qsp.exceptions import WorkflowExceptions
from qsp.utils import Loader


class Sections:
    script_variables = "script_variables"
    script = "script"
    step_name = "name"
    set_file = "set_file"
    steps = "steps"


class Actions:
    def __init__(self, vmanager: dict, sections) -> None:
        self.vmanager = vmanager
        self.sections = sections

    def develop(self, step):
        self.__execute_commands(step)
        self.__set_file(step)

    def __set_file(self, step):
        ...

    def __execute_commands(self, step):
        script_variables = {
            var: self.vmanager[var] for var in step[self.sections.script_variables]
        }

        template = Template(step[self.sections.script])
        commands = template.render(script_variables).split("\n")

        for command in commands:
            try:
                subprocess.check_output(
                    command.split(" "),
                    stderr=subprocess.PIPE,
                )

            except subprocess.CalledProcessError as e:
                error_output = e.stderr.decode("utf-8")
                raise WorkflowExceptions.ScriptFailed(
                    WorkflowExceptions.ScriptFailed.get_message(command, error_output)
                )


class Workflow:
    def __init__(self, workflow_path: str, sections: Sections = Sections) -> None:
        self.sections = sections
        with open(workflow_path, "r") as file:
            self.workflow = yaml.safe_load(file)

    def run(self, vmanager: dict):
        actor = Actions(vmanager, self.sections)
        for step in self.workflow[self.sections.steps]:
            with Loader(
                step[self.sections.step_name], end="Project Started Successfully!"
            ):
                actor.develop(step)
