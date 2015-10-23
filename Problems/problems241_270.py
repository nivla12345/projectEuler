import Tools

__author__ = 'Alvin'


# Find the smallest denominator d which has resilience 15499/94744
def p243():
    prime_sieve_size = 10000000
    # 11 * 1409
    bound_numerator = 15499
    # 94745: 2707 * 5 * 7
    bound_denominator = 94744

    decimal_value = bound_numerator / bound_denominator

    primes = set(Tools.prime_sieve_atkins(prime_sieve_size))

    d = bound_denominator
    while Tools.totient_function(d, primes) / float(d) >= decimal_value:
        d += 2
        if d > prime_sieve_size:
            return 0
    return d
