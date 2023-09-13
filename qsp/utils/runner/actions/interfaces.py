from abc import ABC, abstractmethod

from marshmallow import Schema


class ActionInterface(ABC):
    @abstractmethod
    def get_schema(self) -> Schema:
        ...
