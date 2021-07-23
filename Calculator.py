class Calculator1():
    def add(*val1, **val2):
        sum = 0
        for m in val1:
            sum = sum + m
        for n in val2.values():
            sum = sum + n
        return sum


    def minus(*val1, **val2):
        minus = 0
        for m in val1:
            minus = minus - m
        for n in val2.values():
            minus = minus - n
        return minus


    def mul(*val1, **val2):
        mul = 0
        for m in val1:
            mul = mul * m
        for n in val2.values():
            mul = mul * n
        return mul


    def divisions(*val1, **val2):
        divisions = 0
        for m in val1:
            divisions = divisions / m
        for n in val2.values():
            divisions = divisions / n
        return divisions
