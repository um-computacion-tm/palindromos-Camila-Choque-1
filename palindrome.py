import unittest


def is_palindrome(palabra):

    palabra2 = palabra[::-1]

    if palabra == palabra2:
        return True
    else:
        return False


class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        user_input = "a"
        result = is_palindrome(user_input)
        self.assertTrue(result)

    def test_with_ala(self):
        user_input = "ala"
        result = is_palindrome(user_input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        user_input = "neuquen"
        result = is_palindrome(user_input)
        self.assertTrue(result)

    def test_with_hola(self):
        user_input = "hola"
        result = is_palindrome(user_input)
        self.assertFalse(result)


unittest.main()
