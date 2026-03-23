from typing import List
from src.order_item import OrderItem


class Order:
    def __init__(self, items: List[OrderItem], original_amount: float,
                 discount: float, total_amount: float):
        self.items = items
        self.original_amount = original_amount
        self.discount = discount
        self.total_amount = total_amount
