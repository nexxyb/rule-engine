from .base import BaseRule
from .registry import register_rule


@register_rule
class MinItems2Rule(BaseRule):
    key = "min_items_2"

    def check(self):
        return self.order.items_count >= 2
