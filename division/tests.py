from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from .models import Division
from sknf.validators import check_valid_chars

class DivisionTest(TestCase):

    def test__null_name__should_raise_error(self):
        s = Division(created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__empty_code__should_raise_error(self):
        s = Division(name='', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_name_is_duplicate__should_raise_error(self):
        s = Division(name='Dhaka',created_date=timezone.now())
        s1 = Division(name='Dhaka',created_date=timezone.now())
        with self.assertRaises(IntegrityError):
            s.save()
            s1.save()

    def test__max_length_validation_is__added(self):
        max_length = Division._meta.get_field('name').max_length
        self.assertEquals(max_length, 128)

    def test__100_plus_char_text__should_raise_error(self):
        s = Division(
            name="tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft"
                 " tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg"
                 " sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft ", created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_space___should_pass(self):
        time = timezone.now()
        s = Division( name='A A', created_date=time)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__check_valid_chars__when_dash__should_raise_error(self):
        s = Division(name='A-', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_underscore__should_raise_error(self):
        s = Division(name='Abc_', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_questionsign__should_raise_error(self):
        s = Division(name='A?BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_numeric__should_raise_error(self):
        s = Division(name='123', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_Alpha_Numeric__should_raise_error(self):
        s = Division(name='Abc123', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_comma__should_raise_error(self):
        s = Division(name='A,bcd', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_curly_bracket_first__should_raise_error(self):
        s = Division(name='A{BBB', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_curly_bracket_last__should_raise_error(self):
        s = Division(name='A}BCDE', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_period__should_raise_error(self):
        s = Division(name='A.BCD', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_plus__should_raise_error(self):
        s = Division(name='A+BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_single_quote__should_raise_error(self):
        s = Division(name='A\'BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_double_quote__should_raise_error(self):
        s = Division(name='A"BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_back_slash__should_raise_error(self):
        s = Division(name='A\\BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_equal__should_raise_error(self):
        s = Division(name='A=BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_atsign__should_raise_error(self):
        s = Division(name='A@BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_exclamation_mark__should_raise_error(self):
        s = Division(name='A!BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_hash__should_raise_error(self):
        s = Division(name='A#BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_dollarsymbol__should_raise_error(self):
        s = Division(name='A$BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_slash__should_raise_error(self):
        s = Division(name='A/BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_first_bracket_first__should_raise_error(self):
        s = Division(name='A(BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_percent__should_raise_error(self):
        s = Division(name='A%BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_square_bracket_last__should_raise_error(self):
        s = Division(name='A]BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_square_bracket_fast__should_raise_error(self):
        s = Division(name='A[BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_less_then__should_raise_error(self):
        s = Division(name='A<BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_greater_then__should_raise_error(self):
        s = Division(name='A>BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_ampersand_should_raise_error(self):
        s = Division(name='A&BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_star__should_raise_error(self):
        s = Division(name='A*BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_caret__should_raise_error(self):
        s = Division(name='A^BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_semicolon__should_raise_error(self):
        s = Division(name='A:BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__check_valid_chars__when_tild__should_raise_error(self):
        s = Division(name='A~BC', created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()



