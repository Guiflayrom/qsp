from qsp.exceptions import TemplateException


class WorkflowExceptions:
    class CommandFailed(Exception, TemplateException):
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__(self.message)

        @staticmethod
        def get_message(i1) -> str:
            return f'The command "{i1}" failed'
