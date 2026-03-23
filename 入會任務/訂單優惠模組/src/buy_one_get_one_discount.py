from typing import List
from src.order_item import OrderItem
from src.discount import Discount


class BuyOneGetOneDiscount(Discount):
    def __init__(self, category: str):
        self.category = category

    def calculate_discount(self, items: List[OrderItem]) -> float:
        return 0

    def apply_bonus_items(self, items: List[OrderItem]) -> List[OrderItem]:
        result = []
        for item in items:
            if item.product.category == self.category:
                result.append(OrderItem(product=item.product, quantity=item.quantity + 1))
            else:
                result.append(item)
        return result
