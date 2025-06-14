import math


# Тестирование с помощью pytest
def test_integers():
    res = calculate_average([-1, 2, 8, -49, 75])
    assert res == 7


def test_fractiional_nums():
    res = calculate_average([1.7, 2.0056, -35.0421, 31.49, -7.5])
    assert res == -2


def test_empty_list():
    res = calculate_average([])
    assert res == None


# Основной код программы
def calculate_average(numbers: list[float]) -> float | None:
    if numbers:
        return math.floor(sum(numbers) / len(numbers))
    return None


def show_result(data, numbers):
    if not data:
        return 'Был введён пустой список.'
    else:
        return f'Среднее арифметическое списка {numbers}: {data}'


def main():
    input_str = input("Введите числа через пробел: ")
    numbers = [float(num) for num in input_str.split()]
    result = calculate_average(numbers)
    print(show_result(result))


if __name__ == '__main__':
    main()
