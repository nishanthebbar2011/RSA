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
        self.public_key = 65537 #A very common choice for thr public key. it helps to ensure faster encryption.
        self.private_key = UtilityMath.multiplicative_modular_inverse(self.public_key, self.totient)



    def process_string(self, message):
        """Convert string to long integer
        Args:
            message: string
        REFERENCE
        =========
        https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Util/number.py
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
        REFERENCE
        =========
        https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Util/number.py
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

    def encrypt(self, message, ):
        """
        Encrypts the message using the Public key of the receiver.
        :param message: String
        :return: String
        """
        message  = self.process_string(message)

        if message.bit_length() > self.n.bit_length():
           raise ValueError("Please enter a smaller string!")
        print(message)
        print(UtilityMath.modular_exponentiation(message, self.public_key, self.n))
        return UtilityMath.modular_exponentiation(message, self.public_key, self.n)

    def decrypt(self, ciphertext):
        print(ciphertext)
        print(UtilityMath.modular_exponentiation(ciphertext, self.private_key, self.n))
        return self.recover_string(UtilityMath.modular_exponentiation(ciphertext, self.private_key, self.n))

u = User()

ciphertext = u.encrypt("hello")
print(u.decrypt(ciphertext))

