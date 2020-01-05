from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from districts.models import District
from division.models import Division
from eduplus_activity.models import EduPlusActivity, Method
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from topics.models import Topics


class EduplusActivityTest(TestCase):

    def setUp(self):
        user = User.objects.create(email='test@example.com')
        user.set_password('12345')
        user.user_type = 5
        user.save()
        self.user = user
        admin_user = User.objects.create(email='admin@example.com')
        admin_user.set_password('12345')
        admin_user.user_type = 1
        admin_user.save()
        self.admin_user = admin_user
        div = Division(name='Dhaka')
        div.save()
        self.division = div
        dis = District(division=self.division, name='Gazipur')
        dis.save()
        self.district = dis
        s1 = School(name='Mirpur School', school_id=123, division=self.division, district=self.district)
        s1.save()
        self.school = s1
        edu_activity = EduPlusActivity.objects.create(date=timezone.now(), school=self.school,presence_skleader=True, description='Nothing done')
        skleader = SkLeaderProfile(school=self.school, user=self.user, gender='M', student_class='6',
                                   roll=10, mobile='018152045', image='a.png', joining_date=timezone.now())
        skleader.save()
        sk = SkMemberProfile(school=self.school, user=self.user, gender='M', student_class='6',
                            roll=10, mobile='018152045', image='a.png', joining_date=timezone.now())

        t1= Topics(name='Knowledge')
        t1.save()
        t2= Topics(name='Learning')
        t2.save()

        u1=User(email='A@g.com', user_type= '6')
        u1.save()


    def test__when_school_is_null__should_raise_error(self):
        eplus_activity = EduPlusActivity(date=timezone.now(), presence_skleader=True, description='Nothing done')
        with self.assertRaises(ValidationError):
            eplus_activity.full_clean()

    def test__when_description_is_null__should_raise_error(self):
        eplus_activity = EduPlusActivity(date=timezone.now(), school=self.school, presence_skleader=True)
        with self.assertRaises(ValidationError):
            eplus_activity.full_clean()

    def test__when_description_is_blank__should_raise_error(self):
        eplus_activity = EduPlusActivity(date=timezone.now(), school=self.school, presence_skleader=True, description='')
        with self.assertRaises(ValidationError):
            eplus_activity.full_clean()

    def test__max_length_validation_added__to_description(self):
        max_length = EduPlusActivity._meta.get_field('description').max_length
        self.assertEquals(max_length, 200)

    def test__200_plus_char_text_in_description__should_raise_error(self):
        s = EduPlusActivity(date=timezone.now(),presence_skleader=True,
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
                        "It has survived not only five centuries, but also the leap into electronic "
                        "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the "
                        "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__if_required_data_is_given__should_pass(self):
        topic = Method.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        instance = EduPlusActivity.objects.create(date=timezone.now(), school=self.school,presence_skleader=True, description='Nothing done')

        instance.topics.set(topic)
        instance.attendance.set(user)
        try:
            instance.full_clean()
        except:
            self.fail()

    # #view test

    def test_when__send_get_request_for_eduplus_activity_creation__should_return_status_code_200(self):
        logged_in = self.client.login(email='test@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_add'), follow=True)
        self.assertEquals(eduplus_activity_response.status_code, 200)

    def test_when__request_for_eduplus_activity_invalid_data__should_raise_error(self):
        logged_in = self.client.login(email='test@example.com', password='12345')
        self.assertTrue(logged_in)
        topic = Topics.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        eduplus_activity_response = self.client.post(reverse('eduplus_activity:eduplus_activity_add'), {'date':timezone.now(), 'school':self.school.pk,
                                                                                                        'presence_skleader':True,'attendance':set(user), 'topics':set(topic), 'description':'test'}, follow=True)
        self.assertContains(response=eduplus_activity_response, status_code=200,
                            text='<li class="help-block" style="color:red;margin-bottom: 5px;">Select at least one topic.</li>', html=True)

    def test_when__request_for_eduplus_activity_report_list__should_return_eduplus_activity_list(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_count = EduPlusActivity.objects.count()
        topic = Method.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        instance = EduPlusActivity.objects.create(date=timezone.now(), school=self.school, presence_skleader=True,
                                                  description='Nothing done')
        instance.topics.set(topic)
        instance.attendance.set(user)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_report_list'), follow=True)
        self.assertEqual(EduPlusActivity.objects.count(), eduplus_activity_count + 1)
        self.assertContains(response=eduplus_activity_response, status_code=200,
                            text='<td>Nothing done</td>', html=True)

    def test_when__search_for_eduplus_activity_report_list__should_return_report_list_page_status_code(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_search_list'), follow=True)
        self.assertEquals(eduplus_activity_response.status_code, 200)

    def test_when__school_name_is_searched__should_return_respective_eduplus_activity_list(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_search_list'),
                                                data={'name_contains': 'Mirpur School'}, follow=True)
        self.assertContains(response=eduplus_activity_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)

    def test_when__division_name_is_searched__should_return_respective_eduplus_activity_list(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_search_list'),
                                                data={'division_contains': 'Dhaka'}, follow=True)
        self.assertContains(response=eduplus_activity_response, status_code=200,
                            text='<td>Dhaka</td>', html=True)

    def test_when__district_name_is_searched__should_return_respective_eduplus_activity_list(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_search_list'),
                                                data={'district_contains': 'Gazipur'}, follow=True)
        self.assertContains(response=eduplus_activity_response, status_code=200,
                            text='<td>Gazipur</td>', html=True)

    def test_when__all_are_searched__should_return_respective_eduplus_activity_list(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        eduplus_activity_response = self.client.get(reverse('eduplus_activity:eduplus_activity_search_list'),
                                                data={'name_contains': 'Mirpur School', 'division_contains': 'Dhaka',
                                                      'district_contains': 'Gazipur'}, follow=True)
        self.assertContains(response=eduplus_activity_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)

class MethodTest(TestCase):
    def test__null_name__should_raise_error(self):
        s = Method(created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__uniqe_validation_added(self):
        unique = Method._meta.get_field('name').unique
        self.assertIn(str(unique),'True')

    def test__max_length_validation_added(self):
        max_length = Method._meta.get_field('name').max_length
        self.assertEquals(max_length, 128)