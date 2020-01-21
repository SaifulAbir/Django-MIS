from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from .models import School,User,SkLeaderProfile,SkleaderDetails

class SkleaderProfileTest(TestCase):
    def setUp(self):
        s1= User(user_type=5, email='skleader@gmail.com',username='01712121212')
        s1.save()
        self.user=s1

        s2= School(name='Mirpur School', school_id=123)
        s2.save()
        self.school=s2

        user = User.objects.create(username='01712121211')
        user.set_password('12345')
        user.user_type = 1
        user.save()

    def test__when_Every_field_is_valid___should_pass(self):
        time = timezone.now()
        s = SkLeaderProfile(school=self.school,user=self.user,gender='M',student_class='6',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_Username_is_null__should_raise_error(self):
        s = SkLeaderProfile(school=self.school,gender='M',student_class='6',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_is_null__should_raise_error(self):
        s = SkLeaderProfile(user=self.user,gender='M',student_class='6',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_mobile_is_null__should_raise_error(self):
        s = SkLeaderProfile(user=self.user,school=self.school,gender='M',student_class='6',
                            roll=10,image='a.png',joining_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_mobile_is_empty__should_raise_error(self):
        s = SkLeaderProfile(user=self.user,school=self.school,gender='M',student_class='6',
                            mobile='',roll=10,image='a.png',joining_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_gender_is_null__should_pass(self):
        s = SkLeaderProfile(school=self.school,user=self.user,student_class='6',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_gender_is_empty__should_raise_pass(self):
        s = SkLeaderProfile(school=self.school,user=self.user,student_class='6',gender='',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_student_class_is_null__should_raise_pass(self):
        s = SkLeaderProfile(school=self.school,user=self.user,gender='M',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_student_class_is_empty__should_raise_pass(self):
        s = SkLeaderProfile(school=self.school,user=self.user,gender='M',student_class='',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_roll_is_null__should_raise_pass(self):
        s = SkLeaderProfile(school=self.school,user=self.user,gender='M',student_class='6',
                            mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_roll_is_empty__should_raise_error(self):
        s = SkLeaderProfile(school=self.school,user=self.user,gender='M',student_class='6',
                            roll='',mobile='018152045',image='a.png',joining_date=timezone.now())
        try:
            s.full_clean()
        except:
            self.fail()


    def test__when_school_name_is_searched__should_give_result_accordingly(self):
        s = SkLeaderProfile(school=self.school,user=self.user,gender='M',student_class='6',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        s.save()
        s1=self.client.login(username='01712121211', password='12345')
        response = self.client.get('/skleaders/skleader_list/',{'school_contains':'mirpur'},follow=True)
        self.assertContains(response = response, status_code=200,  text='<td>Mirpur School (123)</td>', html=True)


class SkleaderDetailsTest(TestCase):
    def setUp(self):
        s1 = User(user_type=5, email='head@gmail.com', )
        s1.save()
        self.user = s1

        s2 = School(name='Mirpur School', school_id=123)
        s2.save()
        self.school = s2

        s3 = SkLeaderProfile(school=self.school,user=self.user,gender='M',student_class='6',
                            roll=10,mobile='018152045',image='a.png',joining_date=timezone.now())
        s3.save()
        self.skleader = s3

    def test__when_School_is_null__should_raise_error(self):
        s = SkleaderDetails(skleader=self.skleader,from_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__if_blank_is_added_in_school(self):
        blank = SkleaderDetails._meta.get_field('school').blank
        self.assertEquals(blank, False)

    def test__when_Skleader_is_null__should_raise_error(self):
        s = SkleaderDetails(school=self.school,from_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__if_blank_is_added_in_headmaster(self):
        blank = SkleaderDetails._meta.get_field('skleader').blank
        self.assertEquals(blank, False)

    def test__when_to_date_is_null___should_pass(self):
        time = timezone.now()
        s = SkleaderDetails( school=self.school, skleader= self.skleader, from_date=time)
        try:
            s.full_clean()
        except:
            self.fail()





