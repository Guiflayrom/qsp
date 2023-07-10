from .rules import RulesExceptions
from .workflow import WorkflowExceptions
from abc import ABC, abstractstaticmethod

__all__ = [RulesExceptions, WorkflowExceptions]


class TemplateException(ABC):
    @abstractstaticmethod
    def get_message(self):
        ...
