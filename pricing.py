from decimal import Decimal, ROUND_HALF_UP


def discounted_total(unit_price, quantity, discount):
    price = Decimal(str(unit_price))
    rate = Decimal(str(discount))
    if quantity < 0 or not 0 <= rate <= 1:
        raise ValueError('Invalid quantity or discount')
    discounted_unit = (price * (1 - rate)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return discounted_unit * quantity
