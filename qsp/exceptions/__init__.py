from abc import ABC, abstractstaticmethod

from .rules import RulesExceptions
from .workflow import WorkflowExceptions

__all__ = [RulesExceptions, WorkflowExceptions]


class TemplateException(ABC):
    @abstractstaticmethod
    def get_message(self):
        ...
