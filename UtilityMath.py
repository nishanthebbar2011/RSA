def modular_exponentiation(x, y, n):
    """
    Computes '(x**y)' % n in Log(y) time
    :param x: The base
    :param y: The power
    :param n: n
    :return: Returns result of type int
    """
    result = 1
    while y > 0:
        if y & 1 == 1:
            result =  (result * x) % n

        y = y >> 1
        x = (x * x) % n
    return result

def gcd(a, b):
    """
    Computes and returns the Greatest Common Divisor of two numbers, 'a' and 'b'
    :param a:
    :param b:
    :return: int
    """

    if a > b:
        a, b = b, a

    while a:
        a, b = b % a, a

    return b

def lcm(a, b):
    return (a * b) // gcd(a, b)

def extended_gcd(a, b):
    """
    Computes 'x' and 'y' such that 'ax + by = gcd(a, b)'
    :param a: Integer
    :param b: Integer
    :return: Integers, x and y
    """
    x_prev, x = 0, 1
    y_prev, y = 1, 0

    while a:
        q = b // a
        x, x_prev = x_prev - q * x, x
        y, y_prev = y_prev - q * y, y
        a, b = b % a, a

    return b, x_prev, y_prev


def multiplicative_modular_inverse(e, n):
    """
    Computes and returns the modular inverse of 'e' under Modulo 'n'. Reference: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    :param e: Integer 'e'
    :param n: Integer 'n'
    :return: Integer
    """

    gcd, x, y = extended_gcd(e, n)

    if gcd == 1:
        return (x % n + n) % n
    else:
        raise Exception("Inverse does not exist. Not co-primes")

print(gcd(511, 1421))
