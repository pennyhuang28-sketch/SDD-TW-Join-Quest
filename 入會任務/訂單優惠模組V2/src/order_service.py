from typing import List
from src.order_item import OrderItem
from src.order import Order
from src.discount import Discount


class OrderService:
    def __init__(self, discounts: List[Discount] = None):
        self.discounts = discounts or []

    def checkout(self, items: List[OrderItem]) -> Order:
        original_amount = sum(
            item.product.unit_price * item.quantity for item in items
        )
        total_discount = sum(d.calculate_discount(items) for d in self.discounts)
        bonus_items = list(items)
        for d in self.discounts:
            bonus_items = d.apply_bonus_items(bonus_items)
        total_amount = original_amount - total_discount
        return Order(
            items=bonus_items,
            original_amount=original_amount,
            discount=total_discount,
            total_amount=total_amount,
        )
