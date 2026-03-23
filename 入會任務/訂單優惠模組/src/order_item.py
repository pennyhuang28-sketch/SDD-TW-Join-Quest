from src.product import Product


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        assert quantity > 0
        self.product = product
        self.quantity = quantity
