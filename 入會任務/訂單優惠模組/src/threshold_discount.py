from typing import List
from src.order_item import OrderItem
from src.discount import Discount


class ThresholdDiscount(Discount):
    def __init__(self, threshold: float, discount: float):
        self.threshold = threshold
        self.discount = discount

    def calculate_discount(self, items: List[OrderItem]) -> float:
        subtotal = sum(item.product.unit_price * item.quantity for item in items)
        return self.discount if subtotal >= self.threshold else 0

    def apply_bonus_items(self, items: List[OrderItem]) -> List[OrderItem]:
        return items
