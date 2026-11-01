import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Caesar_Cipher import caesar


class CaesarCipherTests(unittest.TestCase):
    def test_encrypts_and_preserves_case(self):
        self.assertEqual(caesar("Hello, World!", 3), "Khoor, Zruog!")

    def test_decrypts(self):
        self.assertEqual(caesar("Khoor, Zruog!", 3, encrypt=False), "Hello, World!")

    def test_wraps_alphabet(self):
        self.assertEqual(caesar("xyz XYZ", 3), "abc ABC")

    def test_preserves_punctuation_and_digits(self):
        self.assertEqual(caesar("Meet at 5:30.", 2), "Oggv cv 5:30.")

    def test_rejects_invalid_shift(self):
        self.assertEqual(caesar("hello", 0), "Shift must be an integer between 1 and 25.")
        self.assertEqual(caesar("hello", "3"), "Shift must be an integer value.")


if __name__ == "__main__":
    unittest.main()
