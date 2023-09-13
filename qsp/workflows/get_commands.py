# fmt: off

from glob import glob
from os import path
from os.path import splitext
from typing import Dict, Tuple

import yaml
from typer import Typer

from qsp.utils import get_dynamic_function_string
from qsp.utils.cli import (FileArgument, OutputArgument, TypeOption,
                           framework_command)
from qsp.utils.validators import ParamsValidator
from qsp.utils.validators.rules import JustOneOfThese, Need

# fmt: on


def __create_validator(yaml_data: dict) -> ParamsValidator:
    """
    Return a validator of ParamsValidator().
    The goal it's grab all rules from yaml file and feed the validator.
    """
    validator = ParamsValidator()

    try:
        for needs in yaml_data["rules"]["need"]:
            validator.add_rules(Need(*needs))
    except KeyError:
        pass
    try:
        for onlyone in yaml_data["rules"]["onlyone"]:
            validator.add_rules(JustOneOfThese(*onlyone))
    except KeyError:
        pass

    return validator


def __build_parameters(yaml_data) -> Tuple[Dict, Tuple]:
    """
    Returns parameters needed by typer to add in our dynamic function,
    which one is going to be build in `__build_function`

    `params` key it's equivalent our function parameter meanwhile its value it's our typing
    `default` follow the same strategy but the value means the default value
    """
    params = {"output": str, "template": str}
    s = "output: str, template: str,"
    defaults = [OutputArgument(), FileArgument()]

    for parameter in yaml_data["parameters"]:
        if parameter["type"] == "Option":
            params[parameter["name"]] = TypeOption(
                parameter["help"], parameter["category"], False
            )
            s += f'{parameter["name"]}:Option("{parameter["help"]}", "{parameter["category"]}", False), '  # noqa

        try:
            defaults.append(parameter["default"])
        except KeyError:
            defaults.append(False)

    return params, tuple(defaults), s


def __build_typer_function():
    """
    It's responsible for build our dynamic function which one going to be used by
    typer decorator @app.command, to wit, our Typer app.
    The dynamic function gonna be build in "exec()" command, which command, it's in utils file
    """
    frameworks = glob(
        path.join(path.dirname(path.abspath(__file__)), "frameworks", "*")
    )

    for framework in frameworks:
        framework_name = framework.split("\\")[-1]
        instance = Typer()

        workflows = glob(path.join(framework, "*.yml"))

        for workflow in workflows:
            with open(workflow, "r") as f:
                yaml_data = yaml.safe_load(f)

                (
                    _,
                    dynamic_function_defaults,
                    dynamic_function_params_string,
                ) = __build_parameters(yaml_data)

            framework_name = path.basename(path.dirname(workflow))
            function_name = splitext(path.basename(workflow))[0]

            validator = __create_validator(yaml_data)

            exec(
                get_dynamic_function_string(
                    function_name, dynamic_function_params_string
                ),
                {
                    "Option": TypeOption,
                    "instance": instance,
                    "framework_command": framework_command,
                    "validator": validator,
                    "path": path,
                    "workflow": workflow,
                    "dynamic_function_defaults": dynamic_function_defaults,
                    "function_name": function_name,
                },
            )

            yield (instance, framework_name)


def commands_subcommands():
    """
    Return a function generator, which one gonna read all framework workflows files, and return
    a typer instance and the framework name.
    """
    return __build_typer_function()
