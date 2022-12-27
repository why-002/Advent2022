def convert_SNAFU_to_base_10(string: str, place=1):
    if not string:
        return 0
    string, current_num = string[:-1], string[-1]

    if current_num.isdigit():
        return int(current_num) * place + convert_SNAFU_to_base_10(string, place * 5)
    elif current_num == '=':
        return -2 * place + convert_SNAFU_to_base_10(string, place * 5)
    elif current_num == '-':
        return -1 * place + convert_SNAFU_to_base_10(string, place * 5)


def convert_base_10_to_SNAFU(num1: int):
    divisor = 1
    while (num1 // divisor) >= 1:
        divisor *= 5
    magnitudes = []
    while divisor >= 1:
        magnitudes.append(num1 // divisor)
        num1 %= divisor
        divisor //= 5

    magnitudes = magnitudes[::-1]
    print(divisor)
    print(magnitudes)
    for index, value in enumerate(magnitudes):
        if value <= 2:
            magnitudes[index] = str(value)
        elif value == 3:
            magnitudes[index] = '='
            magnitudes[index + 1] += 1
        elif value == 4:
            magnitudes[index] = '-'
            magnitudes[index + 1] += 1
        elif value == 5:
            magnitudes[index] = '0'
            magnitudes[index + 1] += 1
    print(magnitudes)
    if magnitudes[-1] == '0':
        magnitudes = magnitudes[:-1]

    return ''.join(magnitudes[::-1])



def interpret_file(fname):
    with open(fname) as fp:
        file = []
        for line in fp:
            file.append(convert_SNAFU_to_base_10(line.strip()))
    return file


if __name__ == '__main__':
    total_in_int = sum(interpret_file('input25.txt'))
    print(convert_base_10_to_SNAFU(total_in_int))

# not 37503495108131
