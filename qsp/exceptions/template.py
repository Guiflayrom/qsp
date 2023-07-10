from abc import ABC, abstractstaticmethod


class TemplateException(ABC):
    @abstractstaticmethod
    def get_message(self):
        ...
