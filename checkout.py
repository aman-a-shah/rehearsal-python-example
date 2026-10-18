from pricing import discounted_total

def invoice_line(unit_price, quantity, discount):
    return {'total': str(discounted_total(unit_price, quantity, discount)), 'quantity': quantity}
