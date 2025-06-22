from main import AverageCalculating

test = AverageCalculating()


def test_integers():
    test.numbers = [-7, 3, 90, -49, 15]
    res = test.calculate_average()
    assert res == 10


def test_fractiional_nums():
    test.numbers = [1.7, 2.0056, -35.0421, 31.49, -7.5]
    res = test.calculate_average()
    assert res == -2


def test_different_nums():
    test.numbers = [10, -2.007, -35, 78.54, -75]
    res = test.calculate_average()
    assert res == -5


def test_empty_list():
    test.numbers = []
    res = test.calculate_average()
    assert res == None
