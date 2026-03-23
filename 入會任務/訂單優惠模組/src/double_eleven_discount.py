from typing import List
from src.order_item import OrderItem
from src.discount import Discount


class DoubleElevenDiscount(Discount):
    BUNDLE_SIZE = 10
    DISCOUNT_RATE = 0.2

    def calculate_discount(self, items: List[OrderItem]) -> float:
        total_discount = 0
        for item in items:
            bundles = item.quantity // self.BUNDLE_SIZE
            total_discount += bundles * self.BUNDLE_SIZE * item.product.unit_price * self.DISCOUNT_RATE
        return total_discount

    def apply_bonus_items(self, items: List[OrderItem]) -> List[OrderItem]:
        return items
