from abc import ABC, abstractmethod
from typing import List
from src.order_item import OrderItem


class Discount(ABC):
    @abstractmethod
    def calculate_discount(self, items: List[OrderItem]) -> float:
        pass

    @abstractmethod
    def apply_bonus_items(self, items: List[OrderItem]) -> List[OrderItem]:
        pass
