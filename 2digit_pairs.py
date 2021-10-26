def digit_compare(number: str) -> bool:
    return number[:2] == number[2:]


if __name__ == '__main__':
    print('YES' if digit_compare(input()) else 'NO')
