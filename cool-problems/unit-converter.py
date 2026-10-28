
def kmMile(unit, km_val):
     return round(km_val * 0.6213712, 2)

def celsiusFahrenheit(unit, deg):
    if unit == "C":
        return round(deg*9/5 + 32, 2)
    elif unit == "F":
        return round(5*(deg - 32)/9, 2)
    return False
