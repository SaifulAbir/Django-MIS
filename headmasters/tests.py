from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from .models import School,User,HeadmasterProfile,HeadmasterDetails


class HeadMasterProfileTest(TestCase):
    def setUp(self):
        s1= User(user_type=2, email='head@gmail.com',)
        s1.save()
        self.user=s1

        s2= School(name='Mirpur School', school_id=123)
        s2.save()
        self.school=s2

        user = User.objects.create(email='a@g.com')
        user.set_password('12345')
        user.user_type = 1
        user.save()

    def test__when_Every_field_is_valid___should_pass(self):
        time = timezone.now()
        s = HeadmasterProfile(user=self.user,school=self.school,joining_date=timezone.now(),image='1.png',mobile='0181543421')
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_Username_is_null__should_raise_error(self):
        s = HeadmasterProfile(school=self.school,joining_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_School_is_null__should_raise_error(self):
        s = HeadmasterProfile(user=self.user,joining_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Joining_Date_is_null__should_raise_error(self):
        s = HeadmasterProfile(user=self.user,school=self.school)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_Joining_Date_is_empty__should_raise_error(self):
        s = HeadmasterProfile(user=self.user,school=self.school, joining_date='')
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__if_max_leangth_is_added__in_mobile_number(self):
        max_length = HeadmasterProfile._meta.get_field('mobile').max_length
        self.assertEquals(max_length, 11)


    def test__when_school_name_is_searched__should_give_result_accordingly(self):
        s = HeadmasterProfile(user=self.user,school=self.school,joining_date=timezone.now(),image='1.png',mobile='0181543421')
        s.save()

        s1=self.client.login(email='a@g.com', password='12345')
        response = self.client.get('/headmasters/headmaster_list/',{'school_contains':'mirpur'},follow=True)
        self.assertContains(response = response, status_code=200,  text='<td>Mirpur School (123)</td>', html=True)

class HeadmasterDetailsTest(TestCase):
    def setUp(self):
        s1= User(user_type=2, email='head@gmail.com',)
        s1.save()
        self.user=s1

        s2= School(name='Mirpur School', school_id=123)
        s2.save()
        self.school=s2

        s3= HeadmasterProfile(user=self.user, school=self.school,joining_date=timezone.now() )
        s3.save()
        self.headmaster = s3

    def test__when_School_is_null__should_raise_error(self):
        s = HeadmasterDetails(headmaster=self.headmaster,from_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__if_blank_is_added_in_school(self):
        blank = HeadmasterDetails._meta.get_field('school').blank
        self.assertEquals(blank, False)

    def test__when_Headmaster_is_null__should_raise_error(self):
        s = HeadmasterDetails(school=self.school,from_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__if_blank_is_added_in_headmaster(self):
        blank = HeadmasterDetails._meta.get_field('headmaster').blank
        self.assertEquals(blank, False)

    def test__when_From_date_is_null__should_raise_error(self):
        s = HeadmasterDetails(school=self.school,headmaster=self.headmaster)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_to_date_is_null___should_pass(self):
        time = timezone.now()
        s = HeadmasterDetails( school=self.school, headmaster= self.headmaster, from_date=time)
        try:
            s.full_clean()
        except:
            self.fail()












