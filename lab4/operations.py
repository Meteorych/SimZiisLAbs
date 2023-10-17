import main
def find_primitive_element(P):
    for g in range(2, P):
        powers = set()
        is_primitive = True
        for i in range(1, P-1):
            power = (g ** i) % P
            if power in powers:
                is_primitive = False
                break
            powers.add(power)
        if is_primitive:
            return g
    return None


def generate_key(primitive_element):
    power_1 = 17
    power_2 = 15
    A = primitive_element ** power_1 % main.P
    B = primitive_element ** power_2 % main.P

    key_1 = B ** power_1 % main.P
    key_2 = A ** power_2 % main.P

    if key_1 == key_2:
        return key_1

