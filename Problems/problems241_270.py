import Tools

__author__ = 'Alvin'


# Find the smallest denominator d which has resilience 15499/94744
def p243():
    # 11 * 1409
    bound_numerator = 15499
    # 94745: 2707 * 5 * 7
    bound_denominator = 94744

    decimal_value = float(bound_numerator) / bound_denominator
    print decimal_value

    d = 510510
    totient_ratio = (Tools.totient_function(d) / float(d - 1))
    min_ratio = totient_ratio
    while totient_ratio > decimal_value:
        d += 510510
        totient_d = Tools.totient_function(d)
        totient_ratio = totient_d / float(d - 1)
        if totient_ratio < min_ratio:
            min_ratio = totient_ratio
            print d, totient_d, min_ratio
    return d
