class Discount:
    def apply(self, order_type, prise):
        if order_type == 'summer':
            return prise * 0.9
        elif order_type == 'black_friday':
            return prise * 0.7