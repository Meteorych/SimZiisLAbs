import cipher_making


def main():
    keyword = cipher_making.generate_keyword()
    begin_word = cipher_making.making_cipher(keyword)


if __name__ == "__main__":
    main()
