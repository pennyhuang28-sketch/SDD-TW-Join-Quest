from behave import given, when, then
from src.product import Product
from src.order_item import OrderItem
from src.order_service import OrderService
from src.threshold_discount import ThresholdDiscount
from src.buy_one_get_one_discount import BuyOneGetOneDiscount


@given('the buy one get one promotion for cosmetics is active')
def step_bogo_cosmetics(context):
    bogo = BuyOneGetOneDiscount(category='cosmetics')
    existing = getattr(context, 'order_service', None)
    if existing:
        context.order_service = OrderService(discounts=existing.discounts + [bogo])
    else:
        context.order_service = OrderService(discounts=[bogo])


@given('the threshold discount promotion is configured:')
def step_threshold_discount(context):
    row = context.table[0]
    discount = ThresholdDiscount(
        threshold=float(row['threshold']),
        discount=float(row['discount']),
    )
    context.order_service = OrderService(discounts=[discount])


@given('no promotions are applied')
def step_no_promotions(context):
    context.order_service = OrderService(discounts=[])


@when('a customer places an order with:')
def step_place_order(context):
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


@then('the order summary should be:')
def step_order_summary(context):
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


@then('the customer should receive:')
def step_customer_receives(context):
    received = {item.product.name: item.quantity for item in context.order.items}
    for row in context.table:
        name = row['productName']
        expected_qty = int(row['quantity'])
        assert name in received, f"Product '{name}' not found in order items"
        assert received[name] == expected_qty, \
            f"Product '{name}': expected quantity={expected_qty}, got {received[name]}"
