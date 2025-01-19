x: list[int | float] = [2, 3, 4.1, 6.2]
#возм вар как int т и float

def grn_to_usd(value:float)->float|None:
    try:
        conversion_factor = 40
        value = value / conversion_factor
        return value
    except TypeError:
        return None
    
grn_to_usd(23)

