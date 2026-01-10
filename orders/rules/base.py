from abc import ABC, abstractmethod


class BaseRule(ABC):
    key = None

    def __init__(self, order):
        self.order = order

    @abstractmethod
    def check(self) -> bool:
        pass
