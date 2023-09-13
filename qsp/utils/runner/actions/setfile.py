from marshmallow import Schema
from marshmallow_dataclass import class_schema, dataclass

from .interfaces import ActionInterface


class SetFile(ActionInterface):
    @dataclass
    class SetFileInterface:
        target: str
        template: str
        macro: str

    def get_schema(self, step, sections) -> Schema:
        data = []
        for target in step[sections.set_file]:
            schema = class_schema(SetFile.SetFileInterface)
            data.append(schema().load(target))
        return data
