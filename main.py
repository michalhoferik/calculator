
def is_input_valid(value_str: str) -> bool:
    try:
        int(value_str)
        return True
    except ValueError:
        return False


def do_calculation(first_value: int, second_value: int, operator: str) -> int:
    if operator == "+":
        return first_value + second_value

    elif operator == "-":
        return first_value - second_value

    elif operator == "*":
        return first_value * second_value

    elif operator == "/":
        return first_value / second_value

    else:
        return 0


def main():
    operator = input("zadejte operator: ")

    first_value_str = input("zadejte prvni cislo: ")
    if not is_input_valid(first_value_str):
        print("zadal jsi blbou hodnotu")
        return

    second_value_str = input("zadejte druhe cislo: ")
    if not is_input_valid(second_value_str):
        print("zadal jsi blbou hodnotu")
        return

    first_value = int(first_value_str)
    second_value = int(second_value_str)

    result = do_calculation(first_value, second_value, operator)
    print(result)



if __name__ == "__main__":
    main()
