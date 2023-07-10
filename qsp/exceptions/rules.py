from .template import TemplateException


class RulesExceptions:
    class ParameterDoesntExist(Exception, TemplateException):
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__(self.message)

        @staticmethod
        def get_message(i1, i2) -> str:
            return f'The supposed parameter "{i1}" in rule "{i2}" do not exist'

    class RequireParam(Exception, TemplateException):
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__(self.message)

        @staticmethod
        def get_message(i1, i2) -> str:
            return f'"{i1}" requires "{i2}"'

    class ConflictParam(Exception, TemplateException):
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__(self.message)

        @staticmethod
        def get_message(i1, i2, all_i) -> str:
            return f'You tried use "{i1}" and "{i2}", but you can use just one of these: {all_i}'
