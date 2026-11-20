import unittest
import calculator as calc


class TestBasicOperations(unittest.TestCase):
    """Тесты базовых арифметических операций."""

    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-2, 3), 1)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertAlmostEqual(calc.add(0.1, 0.2), 0.3, places=9)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(3, 5), -2)
        self.assertEqual(calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(0, 100), 0)
        self.assertAlmostEqual(calc.multiply(0.5, 0.5), 0.25)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertAlmostEqual(calc.divide(1, 3), 0.3333333, places=6)
        self.assertEqual(calc.divide(-6, 3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)


class TestPowerAndRoot(unittest.TestCase):
    """Тесты возведения в степень и извлечения корня."""

    def test_power(self):
        self.assertEqual(calc.power(2, 10), 1024)
        self.assertEqual(calc.power(9, 0.5), 3)
        self.assertEqual(calc.power(2, -2), 0.25)

    def test_sqrt(self):
        self.assertEqual(calc.sqrt(9), 3)
        self.assertEqual(calc.sqrt(0), 0)
        self.assertAlmostEqual(calc.sqrt(2), 1.4142135, places=6)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            calc.sqrt(-4)


class TestFactorial(unittest.TestCase):
    """Тесты факториала."""

    def test_factorial(self):
        self.assertEqual(calc.factorial(0), 1)
        self.assertEqual(calc.factorial(1), 1)
        self.assertEqual(calc.factorial(5), 120)
        self.assertEqual(calc.factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calc.factorial(-1)

    def test_factorial_not_integer(self):
        with self.assertRaises(ValueError):
            calc.factorial(2.5)


class TestMemory(unittest.TestCase):
    """Тесты операций с памятью."""

    def setUp(self):
        self.mem = calc.Memory()

    def test_initial_value(self):
        self.assertEqual(self.mem.recall(), 0.0)

    def test_save_and_recall(self):
        self.mem.save(42)
        self.assertEqual(self.mem.recall(), 42.0)

    def test_clear(self):
        self.mem.save(99)
        self.mem.clear()
        self.assertEqual(self.mem.recall(), 0.0)

    def test_add_to_memory(self):
        self.mem.save(10)
        self.mem.add_to_memory(5)
        self.assertEqual(self.mem.recall(), 15.0)

    def test_sub_from_memory(self):
        self.mem.save(10)
        self.mem.sub_from_memory(4)
        self.assertEqual(self.mem.recall(), 6.0)

    def test_multiple_operations(self):
        self.mem.add_to_memory(3)
        self.mem.add_to_memory(7)
        self.mem.sub_from_memory(2)
        self.assertEqual(self.mem.recall(), 8.0)


class TestParser(unittest.TestCase):
    """Тесты парсера выражений (теперь он лежит внутри calculator.py)."""

    def test_simple_add(self):
        self.assertEqual(calc.evaluate("2+3"), 5)

    def test_priority(self):
        self.assertEqual(calc.evaluate("2+3*4"), 14)

    def test_parentheses(self):
        self.assertEqual(calc.evaluate("(2+3)*4"), 20)

    def test_unary_minus(self):
        self.assertEqual(calc.evaluate("-5+3"), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc.evaluate("5/0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    