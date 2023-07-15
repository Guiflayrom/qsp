import inspect
from os import path
from typing import Callable

from qsp.utils.runner import Workflow
from qsp.utils.validators import ParamsValidator

from .params_manager import ParamsManager


def framework_command(
    validator: ParamsValidator,
    workflow: str,
    defaults: tuple,
    name: str,
):
    """ """

    def decorator(func: Callable):
        func.__defaults__ = defaults

        def wrapper(**params):
            # Merge file variables with params
            vmanager = ParamsManager(params["template"], params)

            # Validate params
            validator.validate_rules(vmanager.variables)

            # Get workflow path
            intern_path = path.dirname(path.abspath(__file__)).split("\\utils")[0]

            workflow_path = path.join(intern_path, "workflows", workflow)

            # Run workflow
            workflow_planner = Workflow(workflow_path)
            workflow_planner.run(vmanager.variables)

            func.__name__ = name
            func.__defaults__ = defaults

            return func

        wrapper.__signature__ = inspect.signature(func)
        wrapper.__name__ = name

        return wrapper

    return decorator
