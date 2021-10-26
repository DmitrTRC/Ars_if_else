def get_max_digit(number: str) -> str:
    return "Digits are equal" if number[0] == number[1] else str(max(number[0], number[1]))


if __name__ == '__main__':
    print(get_max_digit(input()))
