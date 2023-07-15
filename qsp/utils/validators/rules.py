from abc import ABC, abstractmethod
from functools import wraps
from typing import Callable

from qsp.exceptions import RulesExceptions
from qsp.utils import find_all_strings


def validate_variables_decorator(validate_func) -> Callable:
    @wraps(validate_func)
    def wrapper(self, vmanager):
        self.validate_variables(vmanager)
        return validate_func(self, vmanager)

    return wrapper


class Rule(ABC):
    def __init__(self, *parameters) -> None:
        self._parameters = parameters

    @property
    def parameters(self) -> list:
        return self._parameters

    def validate_variables(self, vmanager: dict) -> None:
        params_existents = vmanager.keys()
        child_name = type(self).__name__
        for parameter_tl in self.parameters:
            for parameter in find_all_strings(parameter_tl):
                if parameter not in params_existents:
                    raise RulesExceptions.ParameterDoesntExist(
                        RulesExceptions.ParameterDoesntExist.get_message(
                            parameter, child_name
                        )
                    )

    @abstractmethod
    def validate(self) -> None:
        ...


class JustOneOfThese(Rule):
    def __init__(self, *items) -> None:
        super().__init__(items)

    @validate_variables_decorator
    def validate(self, vmanager: dict) -> None:
        items = self.parameters[0]
        conditioned = []
        for index, item in enumerate(items):
            _v = vmanager[item]
            if _v and not all(i is False for i in conditioned):
                index_last_item = list(
                    filter(lambda i: conditioned[i], range(len(conditioned)))
                )[0]
                raise RulesExceptions.ConflictParam(
                    RulesExceptions.ConflictParam.get_message(
                        item, items[index_last_item], str(items)
                    )
                )

            conditioned.append(_v)


class Need(Rule):
    def __init__(self, item, *needing) -> None:
        super().__init__(item, needing)

    @validate_variables_decorator
    def validate(self, vmanager: dict) -> None:
        item, requirements = self.parameters
        if vmanager[item]:
            for requires in requirements:
                if not vmanager[requires]:
                    raise RulesExceptions.RequireParam(
                        RulesExceptions.RequireParam.get_message(item, requires)
                    )
