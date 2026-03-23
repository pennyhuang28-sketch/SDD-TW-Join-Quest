from behave import given, when, then
from src.product import Product
from src.order_item import OrderItem
from src.order_service import OrderService
from src.double_eleven_discount import DoubleElevenDiscount


@given('一位用戶購買 {quantity:d} 件相同商品')
def step_given_same_products(context, quantity):
    context.order_service = OrderService(discounts=[])


@given('雙十一優惠 - 購買 {quantity:d} 件相同商品')
def step_given_double11_n_products(context, quantity):
    context.order_service = OrderService(discounts=[])


@given('雙十一優惠：同一種商品每買 10 件，則該 10 件同種商品的價格總和會享有 20% 的折扣')
def step_given_double11_promotion(context):
    discount = DoubleElevenDiscount()
    existing = getattr(context, 'order_service', None)
    if existing:
        context.order_service = OrderService(discounts=existing.discounts + [discount])
    else:
        context.order_service = OrderService(discounts=[discount])


@when('用戶下訂單')
def step_when_place_order(context):
    items = []
    for row in context.table:
        category = row.get('category', 'general')
        product = Product(
            name=row['productName'],
            unit_price=float(row['unitPrice']),
            category=category,
        )
        item = OrderItem(product=product, quantity=int(row['quantity']))
        items.append(item)
    context.order = context.order_service.checkout(items)


@when('用戶購買商品 A, B, C, D, E, F, G, H, I, J 各一件（總共十件商品），每一件價格皆為 100 元')
def step_when_10_different_products(context):
    items = [
        OrderItem(product=Product(name=name, unit_price=100.0, category='general'), quantity=1)
        for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    ]
    context.order = context.order_service.checkout(items)


@then('總訂單的價格應為 {amount:d} 元')
def step_then_total_price(context, amount):
    row = context.table[0]
    if 'totalAmount' in row.headings:
        assert context.order.total_amount == float(row['totalAmount']), \
            f"Expected totalAmount={row['totalAmount']}, got {context.order.total_amount}"
    if 'originalAmount' in row.headings:
        assert context.order.original_amount == float(row['originalAmount']), \
            f"Expected originalAmount={row['originalAmount']}, got {context.order.original_amount}"
    if 'discount' in row.headings:
        assert context.order.discount == float(row['discount']), \
            f"Expected discount={row['discount']}, got {context.order.discount}"
