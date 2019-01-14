import Primality
import UtilityMath
from struct import unpack, pack
class User:
    """

    """
    def __init__(self):
        self.p = Primality.generate_large_prime()
        self.q = Primality.generate_large_prime()
        self.n = self.p * self.q
        self.totient = UtilityMath.lcm(self.p - 1, self.q - 1)#Reference: Euler Totient Function -https://en.wikipedia.org/wiki/Carmichael_function
        self.public_key = 65537, self.n #A very common choice for thr public key. it helps to ensure faster encryption.
        self.__private_key = UtilityMath.multiplicative_modular_inverse(self.public_key[0], self.totient)



    def process_string(self, message):
        """Convert string to long integer
        Args:
            message: string
        :return
            Int: Integer representation, corresponding to the string.
        REFERENCE
        =========
        https://github.com/kaushiksk/rsasim/blob/master/rsasim/rsa.py
        """

        acc = 0
        length = len(message)
        if length % 4:
            extra = (4 - length % 4)
            message = bytes('\000', 'utf-8') * extra + bytes(message, 'utf-8')

        for i in range(0, length, 4):
            acc = (acc << 32) + unpack('>I', message[i:i + 4])[0]

        return acc

    @classmethod
    def recover_string(self, number):
        """Convert long to byte string
        Args:
                number: long integer to convert to string
        :return
                String: Message, corresponding to the integer.
        REFERENCE
        =========
        https://github.com/kaushiksk/rsasim/blob/master/rsasim/rsa.py
        """

        s = bytes('', 'utf-8')
        while number > 0:
            s = pack('>I', number & 0xffffffff) + s
            number = number >> 32

        # remove padded zeros
        i = 0
        while i < len(s):
            if s[i] != bytes('\000', 'utf-8')[0]:
                break
            i += 1
        return s[i:]

    def encrypt(self, message, public_key):
        """
        Encrypts the message using the Public key of the receiver.
        :param message: String
        :return: String
        """
        message  = self.process_string(message)

        if message.bit_length() > self.n.bit_length():
           raise ValueError("Please enter a smaller string!")
        return UtilityMath.modular_exponentiation(message, public_key[0], public_key[1])

    def decrypt(self, ciphertext):
        return self.recover_string(UtilityMath.modular_exponentiation(ciphertext, self.__private_key, self.n))

    def sign(self, message):
        return UtilityMath.modular_exponentiation(hash(self.process_string(message)), self.__private_key, self.n)

    def verify(self, message, signed_message, public_key):
        if UtilityMath.modular_exponentiation(signed_message, public_key[0], public_key[1]) == hash(self.process_string(message)):
            print("The integrity of the message has been verified")
            return True
        return False


