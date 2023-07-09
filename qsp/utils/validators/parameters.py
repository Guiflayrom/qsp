from typing import List

from .rules import Rule


class ParamsValidator:
    def __init__(self, vmanager) -> None:
        self.vmanager = vmanager
        self.rules = []

    def add_rules(self, *rules: List[Rule]):
        for rule in rules:
            rule.validate(self.vmanager)
            self.rules.append(rule)
