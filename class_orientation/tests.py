from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from.models import ClassOrientation,School

class ClassOrientationTest(TestCase):

    def setUp(self):
        s1 = School(name='Mirpur School', school_id=123)
        s1.save()
        self.school = s1

    def test__when_school_is_null__should_raise_error(self):
        s = ClassOrientation(created_date=timezone.now(),student_class='7', topic='asd', )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_topic_is_null__should_raise_error(self):
        s = ClassOrientation(created_date=timezone.now(),student_class='7', school=self.school, )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_topic_is_empty__should_raise_error(self):
        s = ClassOrientation(topic='', created_date=timezone.now(),student_class='7', school=self.school,)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_class_is_null__should_raise_error(self):
        s = ClassOrientation(created_date=timezone.now(),topic='asd', school=self.school, )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__128_plus_char_text_in_topic__should_raise_error(self):
        s = ClassOrientation(
            topic="tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft"
                 " tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg"
                 " sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft ", created_date=timezone.now(),student_class='7', school=self.school,)
        with self.assertRaises(ValidationError):
            s.full_clean()







