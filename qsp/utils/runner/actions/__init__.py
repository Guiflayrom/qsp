import subprocess
from os import makedirs, path

import jinja2schema
from jinja2 import Template

from qsp.exceptions import WorkflowExceptions
from qsp.workflows import MACROS_DJANGO

from .setfile import SetFile


class Sections:
    script_variables = "script_variables"
    script = "script"
    step_name = "name"
    workflow_name = "name"
    set_file = "set_file"
    steps = "steps"
    macro = "macro"
    set_file_variables = "set_file_variables"


class Actions:
    def __init__(self, vmanager: dict, sections) -> None:
        self.vmanager = vmanager
        self.sections = sections

    def develop(self, step):
        for action in step.keys():
            match action:
                case "script":
                    self.__execute_commands(step)
                case "macro":
                    self.__execute_macro(step=step)
                case "set_file":
                    self.__set_file(step)

    def __execute_macro(self, macroname=None, step=None) -> dict:
        if not macroname and not step:
            raise TypeError("Macroname And Step Are Equal None.")

        if step:
            macroname = step[self.sections.macro]

        for macro in MACROS_DJANGO:
            if macro.__name__ == macroname.replace("\n", ""):
                return macro(**self.vmanager)

    def __set_file(self, step):
        action = SetFile()
        schema = action.get_schema(step, self.sections)

        for table in schema:
            macro_variables: dict = self.__execute_macro(table.macro)

            with open(table.template, "r", encoding="utf8") as f:
                context_required = jinja2schema.infer(f.read()).keys()

            inclusion = all(
                elemento in macro_variables.keys() for elemento in context_required
            )

            if not inclusion:
                raise WorkflowExceptions.RequiredByTemplateVariablesAreMissing(
                    WorkflowExceptions.RequiredByTemplateVariablesAreMissing.get_message(
                        table.macro, table.template
                    )
                )

            if self.sections.set_file_variables in step.keys():
                path_template = Template(table.target)
                set_file_variables = {
                    var: self.vmanager[var] for var in step[self.sections.set_file_variables]
                }
                table.target = path_template.render(set_file_variables)

            if not path.exists(table.target):
                makedirs("\\".join(table.target.split("\\")[:-1]))

            with open(table.target, "w", encoding="utf8") as target_file:
                with open(table.template, "r", encoding="utf8") as template_file:
                    template = Template(template_file.read())

                target_file.write(template.render(macro_variables))

    def __execute_commands(self, step):
        try:
            script_variables = {
                var: self.vmanager[var] for var in step[self.sections.script_variables]
            }

            template = Template(step[self.sections.script])
            commands = template.render(script_variables).split("\n")

        except KeyError:
            template = Template(step[self.sections.script])
            commands = template.render().split("\n")

        for command in commands:
            try:
                subprocess.check_output(
                    command.split(" "), stderr=subprocess.PIPE, shell=True
                )

            except subprocess.CalledProcessError as e:
                # error_output = e.stderr.decode("utf-8")
                raise WorkflowExceptions.ScriptFailed(
                    WorkflowExceptions.ScriptFailed.get_message(command, str(e))
                )
