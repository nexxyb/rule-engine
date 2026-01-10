from .base import BaseRule
from .registry import register_rule


@register_rule
class MinTotal100Rule(BaseRule):
    key = "min_total_100"

    def check(self):
        return self.order.total > 100
