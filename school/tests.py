from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase, Client
from django.utils import timezone
from.models import School, Division, District , Upazilla, Union,SchoolPost
from.views import school_list

class SchoolTest(TestCase):
    def setUp(self):
        s1 = Division(name='Dhaka')
        s1.save()
        self.division = s1

        s2 = District(division=self.division, name='Gazipur')
        s2.save()
        self.district = s2

        s3 = Upazilla(division=self.division, district=self.district, name='Sripur')
        s3.save()
        self.upazilla = s3

        s4 = Union(division=self.division, district=self.district,upazilla=self.upazilla, name= 'Dholapur')
        s4.save()
        self.union = s4

        self.client = Client()


    def test__when_school_name_is_null__should_raise_error(self):
        s = School(school_id = 123)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_name_is_empty__should_raise_error(self):
        s = School( name='', school_id = 123)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_id_is_null__should_raise_error(self):
        s = School(name = 'Mirpur School')
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_id_is_empty__should_raise_error(self):
        s = School( name='Mirpur School', school_id = '')
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_school_name_is_duplicate__should_raise_error(self):
        sl1 = School( name='Mirpur School', school_id = 123)
        sl2 = School( name='Mirpur School', school_id = 12)
        with self.assertRaises(IntegrityError):
            sl1.save()
            sl2.save()

    def test__when_school_code_is_duplicate__should_raise_error(self):
        sl1 = School( name='Mirpur School', school_id = 123)
        sl2 = School( name='agranee School', school_id = 123)
        with self.assertRaises(IntegrityError):
            sl1.save()
            sl2.save()

    def test__max_length_validation_is__added_for_school_name(self):
        max_length = School._meta.get_field('name').max_length
        self.assertEquals(max_length, 264)

    def test__max_length_validation_is__added_for_school_id(self):
        max_length = School._meta.get_field('school_id').max_length
        self.assertEquals(max_length, 255)

    def test__max_length_validation_is__added_for_school_address(self):
        max_length = School._meta.get_field('address').max_length
        self.assertEquals(max_length, 200)

    def test__when_Division_is_null___should_pass(self):
        time = timezone.now()
        s = School( name='Mirpur School',school_id='123', district=self.district,
                    upazilla=self.upazilla, union = self.union, address='abc', created_date=time,)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_District_is_null___should_pass(self):
        time = timezone.now()
        s = School( name='Mirpur School',school_id='123', division=self.division,
                    upazilla=self.upazilla, union = self.union, address='abc', created_date=time,)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_Upazilla_is_null___should_pass(self):
        time = timezone.now()
        s = School( name='Mirpur School',school_id='123', division=self.division,
                    district=self.district, union = self.union, address='abc', created_date=time,)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_Union_is_null___should_pass(self):
        time = timezone.now()
        s = School( name='Mirpur School',school_id='123', division=self.division,
                    district=self.district, upazilla = self.upazilla, address='abc', created_date=time,)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_address_is_null___should_pass(self):
        time = timezone.now()
        s = School( name='Mirpur School',school_id='123', division=self.division,
                    district=self.district, upazilla = self.upazilla, union=self.union, created_date=time,)
        try:
            s.full_clean()
        except:
            self.fail()

    def test__when_Establishment_date_is_null___should_pass(self):
        time = timezone.now()
        s = School( name='Mirpur School',school_id='123', division=self.division,
                    district=self.district, upazilla = self.upazilla, union=self.union, created_date=time,)
        try:
            s.full_clean()
        except:
            self.fail()

    # def test__when_name_is_searched__should_give_result_accordingly(self):
    #     s = School(name='Mirpur School', school_id='123', division=self.division,
    #                district=self.district, upazilla=self.upazilla, union=self.union, )
    #
    #     s1=self.client.login(username='admin', password='123')
    #     response = self.client.get('school:school_list',{})
    #     self.assertEqual(response,200)




class SchoolPostTest(TestCase):

    def setUp(self):
        s1 = School(name='Mirpur School', school_id= '123')
        s1.save()
        self.school = s1

    def test__when_school_is_null__should_raise_error(self):
        s = SchoolPost(text = 'Hello', created_date=timezone.now() )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_text_is_null__should_raise_error(self):
        s = SchoolPost(school=self.school, created_date=timezone.now() )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_text_is_empty__should_raise_error(self):
        s = SchoolPost(school=self.school, text='', created_date=timezone.now() )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__max_length_validation_is__added_for_school_name(self):
        max_length = SchoolPost._meta.get_field('text').max_length
        self.assertEquals(max_length, 264)














