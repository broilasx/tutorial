import pytest
from tutorial import is_prime


class TestIsPrime:
    """Test suite for the is_prime function."""
    
    # Test numbers less than 2
    def test_negative_number(self):
        """Test that negative numbers return False."""
        assert is_prime(-5) is False
        assert is_prime(-1) is False
    
    def test_zero(self):
        """Test that zero returns False."""
        assert is_prime(0) is False
    
    def test_one(self):
        """Test that one returns False."""
        assert is_prime(1) is False
    
    # Test small prime numbers
    def test_two_is_prime(self):
        """Test that 2 is prime (smallest prime)."""
        assert is_prime(2) is True
    
    def test_small_primes(self):
        """Test small prime numbers."""
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            assert is_prime(prime) is True
    
    # Test composite numbers (non-primes)
    def test_small_composites(self):
        """Test small composite numbers."""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for composite in composites:
            assert is_prime(composite) is False
    
    # Test larger numbers
    def test_large_prime(self):
        """Test a larger prime number."""
        assert is_prime(97) is True
        assert is_prime(541) is True
    
    def test_large_composite(self):
        """Test larger composite numbers."""
        assert is_prime(100) is False
        assert is_prime(121) is False  # 11 * 11
        assert is_prime(1000) is False
    
    def test_even_numbers(self):
        """Test that even numbers (except 2) are not prime."""
        assert is_prime(2) is True
        for even in [4, 6, 8, 10, 100, 1000]:
            assert is_prime(even) is False
    
    def test_perfect_squares(self):
        """Test perfect squares of primes."""
        assert is_prime(4) is False   # 2²
        assert is_prime(9) is False   # 3²
        assert is_prime(25) is False  # 5²
        assert is_prime(49) is False  # 7²
    
    # Additional edge cases
    def test_twin_primes(self):
        """Test twin primes (primes that differ by 2)."""
        twin_prime_pairs = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
        for p1, p2 in twin_prime_pairs:
            assert is_prime(p1) is True
            assert is_prime(p2) is True
    
    def test_products_of_two_primes(self):
        """Test products of two primes (semiprimes)."""
        semiprimes = [6, 15, 21, 35, 77, 143]  # 2×3, 3×5, 3×7, 5×7, 7×11, 11×13
        for semiprime in semiprimes:
            assert is_prime(semiprime) is False
    
    def test_consecutive_numbers(self):
        """Test consecutive number sequences."""
        # All numbers from 2-10 with expected results
        expected = {2: True, 3: True, 4: False, 5: True, 6: False, 
                   7: True, 8: False, 9: False, 10: False}
        for num, is_prime_expected in expected.items():
            assert is_prime(num) is is_prime_expected
    
    def test_numbers_near_boundaries(self):
        """Test numbers at specific boundary values."""
        assert is_prime(2) is True      # First prime
        assert is_prime(3) is True      # Second prime
        assert is_prime(50) is False    # Mid-range composite
        assert is_prime(51) is False    # 3 × 17
        assert is_prime(97) is True     # Largest 2-digit prime
        assert is_prime(98) is False    # 2 × 49
        assert is_prime(99) is False    # 9 × 11
    
    def test_powers_of_two(self):
        """Test powers of 2 (all composite except 2 itself)."""
        powers_of_two = [2, 4, 8, 16, 32, 64, 128, 256, 512]
        for num in powers_of_two:
            if num == 2:
                assert is_prime(num) is True
            else:
                assert is_prime(num) is False
    
    def test_numbers_near_primes(self):
        """Test numbers just before and after known primes."""
        test_cases = [
            (4, False),    # Before 5
            (5, True),
            (6, False),    # After 5
            (12, False),   # Before 13
            (13, True),
            (14, False),   # After 13
        ]
        for num, expected in test_cases:
            assert is_prime(num) is expected
    
    def test_known_large_primes(self):
        """Test some known medium-to-large primes."""
        large_primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
        for prime in large_primes:
            assert is_prime(prime) is False
    
    def test_primes_with_repeated_factors(self):
        """Test composites with repeated prime factors."""
        # Powers of primes
        assert is_prime(8) is False     # 2³
        assert is_prime(27) is False    # 3³
        assert is_prime(32) is False    # 2⁵
        assert is_prime(125) is False   # 5³
    
    def test_moderate_composites(self):
        """Test various composite numbers in mid-range."""
        composites = [22, 24, 26, 28, 33, 35, 39, 45, 51, 57, 63, 65, 69, 75]
        for num in composites:
            assert is_prime(num) is False
