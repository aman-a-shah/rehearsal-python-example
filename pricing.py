from decimal import Decimal, ROUND_HALF_UP


def discounted_total(unit_price, quantity, discount):
    price = Decimal(str(unit_price))
    rate = Decimal(str(discount))
    if quantity < 0 or not 0 <= rate <= 1:
        raise ValueError('Invalid quantity or discount')
    subtotal = price * quantity * (1 - rate)
    return subtotal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
