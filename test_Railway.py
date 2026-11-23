
from Railway import calculate_fare, generate_pnr


def test_calculate_fare():
    assert calculate_fare(2, 500) == 1000
    assert calculate_fare(3, 200) == 600
    assert calculate_fare(1, 500) == 500


def test_invalid_seats():
    try:
        calculate_fare(0, 500)
        assert False
    except ValueError:
        pass


def test_invalid_fare():
    try:
        calculate_fare(2, 0)
        assert False
    except ValueError:
        pass


def test_generate_pnr():
    pnr = generate_pnr()
    assert 100000 <= pnr <= 999999


if __name__ == "__main__":
    test_calculate_fare()
    test_invalid_seats()
    test_invalid_fare()
    test_generate_pnr()

    print("All test cases passed successfully!")
