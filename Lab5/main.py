from generate_big_prime_number import generate_prime


class RSA:
    def __init__(self, p: int, q: int) -> None:
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.f = (self.p - 1) * (self.q - 1)

    def generate_keys(self) -> None:
        self.e = generate_prime([2, self.f])
        self.public_key = (self.e, self.n)

        self.d = pow(self.e, -1, self.f)
        self.private_key = (self.d, self.n)

    def save(self) -> None:
        with open('rsa/open_key', 'w') as f:
            f.write(str(self.public_key))
        with open('rsa/close_key', 'w') as f:
            f.write(str(self.private_key))
        with open('rsa/encrypted_message', 'w') as f:
            f.write(' '.join([str(i) for i in self.ecnrypt_message]))
        with open('rsa/decrypted_message', 'w') as f:
            f.write(self.decrypted_message)
        with open('rsa/digital_signature', 'w') as f:
            f.write(self.digital_sign[0].decode())
            f.write(str(self.digital_sign[1]))

    def encrypt(self, message: str) -> None:
        bytes_text = message.encode()
        self.ecnrypt_message = []
        for i in bytes_text:
            encrypted_char = pow(i, self.public_key[0], self.public_key[1])
            self.ecnrypt_message.append(encrypted_char)

    def decrypt(self) -> None:
        bytes_text = self.ecnrypt_message
        plantext = []
        for i in bytes_text:
            decrypted_char = pow(i, self.private_key[0], self.private_key[1])
            plantext.append(decrypted_char)
        self.decrypted_message = bytes(plantext)
        self.decrypted_message = self.decrypted_message.decode()

    def digital_signature(self, message: str) -> None:
        bytes_text = message.encode()
        self.s = []
        for i in bytes_text:
            encrypted_char = pow(i, self.private_key[0], self.private_key[1])
            self.s.append(encrypted_char)
        self.digital_sign = (bytes_text, self.s)

    def check_digital_signature(self) -> bool:
        plantext = []
        for i in self.digital_sign[1]:
            decrypted_char = pow(i, self.public_key[0], self.public_key[1])
            plantext.append(decrypted_char)
        self.message = bytes(plantext)
        self.message = self.message.decode()
        return self.message == self.digital_sign[0].decode()


def main():
    KEY_SIZE = 1024
    while True:
        p = generate_prime([2**(KEY_SIZE-1)+1, 2**KEY_SIZE - 1])
        q = generate_prime([2**(KEY_SIZE-1)+1, 2**KEY_SIZE - 1])
        if p != q:
            break
    rsa = RSA(p=p, q=q)
    rsa.generate_keys()

    message = ('RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest,'
               'that is widely used for secure data transmission.')
    rsa.encrypt(message=message)
    rsa.decrypt()
    print('Создание цфировой подписи...')
    rsa.digital_signature(message=message)
    print('Подпись готова')
    print(f'Исходный текст - {message}')
    print('Проверка подписи...')
    print('Всё отлично') if rsa.check_digital_signature() else print('Эмм, всё плохо...')
    rsa.save()


if __name__ == '__main__':
    main()