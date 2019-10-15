import unittest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .validators import check_valid_chars


class ValidatorTest(unittest.TestCase):
    def test__check_valid_chars__when_alphabet_only__should_pass(self):
        try:
            check_valid_chars('add')
        except:
            self.fail()

    def test__check_valid_chars__when_number_only__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('555')

    def test__check_valid_chars__when_alphanumeric__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab56')

    def test__check_valid_chars__when_dash__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab5-')

    def test__check_valid_chars__when_underscore__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab5_')

    def test__check_valid_chars__when_space__should_passl(self):
        try:
            check_valid_chars('add b')
        except:
            self.fail()

    def test__check_valid_chars__when_questionsign__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab?5 ')

    def test__check_valid_chars__when_comma__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('b5,')

    def test__check_valid_chars__when_curly_bracket_first__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab{')

    def test__check_valid_chars__when_curly_bracket_last__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab}')

    def test__check_valid_chars__when_period__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab.d')

    def test__check_valid_chars__when_plus__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab+d')

    def test__check_valid_chars__when_single_quote__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab\'d')

    def test__check_valid_chars__when_double_quote__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab"d')

    def test__check_valid_chars__when_back_slash__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab\\')

    def test__check_valid_chars__when_equal__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab=d')

    def test__check_valid_chars__when_atsign__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab@')

    def test__check_valid_chars__when_exclamation_mark__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab!')

    def test__check_valid_chars__when_hash__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab#')

    def test__check_valid_chars__when_dollarsymbol__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab$')

    def test__check_valid_chars__when_slash__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab/')

    def test__check_valid_chars__when_percent__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab%')

    def test__check_valid_chars__when_first_bracket_first__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab(')

    def test__check_valid_chars__when_first_bracket_last__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab)')

    def test__check_valid_chars__when_square_bracket_fast__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab[')

    def test__check_valid_chars__when_square_bracket_last__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab]')

    def test__check_valid_chars__when_less_then__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab<')

    def test__check_valid_chars__when_greater_then__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab>')

    def test__check_valid_chars__when_ampersand_should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab&')

    def test__check_valid_chars__when_star__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab*')

    def test__check_valid_chars__when_semicolon__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab:')

    def test__check_valid_chars__when_caret__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab^')

    def test__check_valid_chars__when_tild__should_fail(self):
        with self.assertRaises(ValidationError):
            check_valid_chars('ab~')



