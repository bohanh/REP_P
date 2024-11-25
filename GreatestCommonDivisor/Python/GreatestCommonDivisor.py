import math

# Test cases for math.gcd function
def test_gcd():
    test_cases = [
        (12, 18),  # gcd(12, 18) = 6
        (60, 48),  # gcd(60, 48) = 12
        (101, 103),  # gcd(101, 103) = 1, prime numbers
        (0, 5),  # gcd(0, 5) = 5
        (5, 0),  # gcd(5, 0) = 5
        (35, 10),  # gcd(35, 10) = 5
    ]

    for a, b in test_cases:
        result = math.gcd(a, b)
        print(f"gcd({a}, {b}) = {result}")

# Run the tests
if __name__ == "__main__":
    test_gcd()
