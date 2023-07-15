from .template import TemplateException


class WorkflowExceptions:
    class ScriptFailed(Exception, TemplateException):
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__(self.message)

        @staticmethod
        def get_message(i1, i2) -> str:
            return f'The command "{i1}" failed\n{i2}'
