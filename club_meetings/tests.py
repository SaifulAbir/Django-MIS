from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from.models import ClubMeetings,School,Topics,User

class ClubMeetingsTest(TestCase):

    def setUp(self):
        s1 = School(name='Mirpur School', school_id=123)
        s1.save()
        self.school = s1

        t1= Topics(name='Knowledge')
        t1.save()
        t2= Topics(name='Learning')
        t2.save()

        u1=User(email='A@g.com', user_type= '6')
        u1.save()


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

    def test__if_required_field_are_given__should_pass(self):
        topic = Topics.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        instance = ClubMeetings.objects.create(school=self.school,class_room='105')

        instance.topics.set(topic)
        instance.attendance.set(user)
        try:
            instance.full_clean()
        except:
            self.fail()