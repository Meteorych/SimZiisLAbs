import operations

P = 8581
def main():
    primitive_element = operations.find_primitive_element(P)
    print(f"PRIMITIVE: {primitive_element}")
    key = operations.generate_key(primitive_element)
    print(f"KEY: {key}")


if __name__ == "__main__":
    main()
