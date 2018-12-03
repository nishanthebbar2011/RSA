import Primality
import UtilityMath
class User:
    """

    """
    def __init__(self):
        self.p = Primality.generate_large_prime()
        self.q = Primality.generate_large_prime()
        self.n = self.p * self.q
        self.totient = UtilityMath.lcm(self.p - 1, self.q - 1)#Reference: Euler Totient Function -https://en.wikipedia.org/wiki/Carmichael_function
        self.public_key = 65537 #A very common choice for thr public key. it helps to ensure faster encryption.
        self.private_key = UtilityMath.multiplicative_modular_inverse(self.public_key, self.totient)

    def encrypt(self, message):
        """
        Encrypts the message using the Public key of the receiver.
        :param message: String
        :return: String
        """

        pass

    def decrypt(self, ciphertext):
        pass

u = User()
