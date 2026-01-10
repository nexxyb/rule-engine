from .base import BaseRule
from .registry import register_rule


@register_rule
class TotalDivisibleBy5Rule(BaseRule):
    key = "total_divisible_by_5"

    def check(self):
        return self.order.total % 5 == 0
