from typing import List

from .rules import Rule


class ParamsValidator:
    """
    Parameters validator, checker whether the rules are valid.
    \nFunctions:\n
    - add_rules()
    - validate_rules()
    """

    def __init__(self) -> None:
        self.rules = []

    def add_rules(self, *rules: List[Rule]):
        for rule in rules:
            self.rules.append(rule)

    def validate_rules(self, vmanager):
        for rule in self.rules:
            rule.validate(vmanager)
