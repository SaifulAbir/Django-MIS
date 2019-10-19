from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from.models import ClubMeetings,School,Topics

class ClubMeetingsTest(TestCase):

    def setUp(self):
        s1 = School(name='Mirpur School', school_id=123)
        s1.save()
        self.school = s1

    def test__when_school_is_null__should_raise_error(self):
        s = ClubMeetings(date=timezone.now(),class_room='7', )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__100_plus_char_text_in_class_room__should_raise_error(self):
        s = ClubMeetings(
            class_room="tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft"
                 " tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg"
                 " sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft sdfgsdg sgddft tesg"
                 " sdfgsdg sgddft ", date=timezone.now(),)
        with self.assertRaises(ValidationError):
            s.full_clean()