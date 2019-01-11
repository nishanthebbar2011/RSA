import random
import UtilityMath

def choose_r(n):
    """
    Needed for Miller-Rabin's.
    Returns greatest 'r' such that (n - 1) == (2**r) * d
    :param n:
    :return:
    """
    r = 1
    while n % 2 == 0:
        r += 1
        n = n // 2
    return r - 1


def miller_rabins(n, k = 40):
    """
    MIller Rabin's Primality test can be found here. https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    It is a probabibilistic method for testing primality.
    :param
        'n': Number whose primality is to be determined
        'k': Parameter that describes the accuracy of the Miller Rabin's test https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    """
    r = choose_r(n - 1) #Express 'n - 1' in the form of ((2**r) * d), where 'd  is odd
    d = (n - 1) // (2**r)
    for i in range(k):
        a = random.randint(2, n - 2)
        x = UtilityMath.modular_exponentiation(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True





def is_prime(n):
    """
    Returns whether a number is Prime or not. Uses Miller-Rabin's test for Primality
    :param n: Number whose Primality is to be determined
    :return: Boolean
    """
    return miller_rabins(n)



def generate_large_prime(number_of_bits = 256):
    """
    Returns a very large prime number.
    :param number_of_bits: Total  number of bits in the large prime. 256 is ideal for the scope of this project
    :return: Int
    """

    prob_prime = 1
    for i in range(1, number_of_bits):
        prob_prime = prob_prime << 1
        prob_prime = prob_prime | random.randint(0,1)

    prob_prime = prob_prime | 1 #Make Sure it is an odd number

    while not is_prime(prob_prime):
        prob_prime += 2

    return prob_prime



