from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from skleaders.models import SkLeaderProfile
from topics.models import Topics
from.models import ClassOrientation,School

class ClassOrientationTest(TestCase):

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
        s1 = School(name='Mirpur School', school_id=123)
        s1.save()
        self.school = s1
        skleader = SkLeaderProfile(school=self.school, user=self.user, gender='M', student_class='6',
                                   roll=10, mobile='018152045', image='a.png', joining_date=timezone.now())
        skleader.save()
        to = Topics.objects.all()
        co = ClassOrientation.objects.create(created_date=timezone.now(), place='1', school=self.school )
        co.topic.set(to)
        self.class_orientation = co

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

    # view test
    def test_class_orientation_add_page_status_code_content_type(self):
        logged_in = self.client.login(email='test@example.com', password='12345')
        self.assertTrue(logged_in)
        orientation_add_response = self.client.get('/class_orientation/add/', follow=True)
        self.assertEquals(orientation_add_response.status_code, 200)
        self.assertEquals(orientation_add_response['Content-Type'], 'application/json')

    def test_class_orientation_update_page_status_code_content_type(self):
        logged_in = self.client.login(email='test@example.com', password='12345')
        self.assertTrue(logged_in)
        orientation_update_response = self.client.get(reverse('class_orientation:class_orientation_update',
                                                              args=(self.class_orientation.id,)), follow=True)
        self.assertEquals(orientation_update_response.status_code, 200)
        self.assertEquals(orientation_update_response['Content-Type'], 'application/json')

    def test_when__request_for_class_orientation_report_list__should_return_class_orientation_list(self):
        logged_in = self.client.login(username='admin@example.com', password='12345')
        self.assertTrue(logged_in)
        class_orientation_count = ClassOrientation.objects.count()
        topic = Topics.objects.exclude(name='')
        instance = ClassOrientation.objects.create(created_date=timezone.now(), place='1', school=self.school)
        instance.topic.set(topic)
        class_orientation_response = self.client.get(reverse('class_orientation:class_orientation_report_list'), follow=True)
        self.assertEqual(ClassOrientation.objects.count(), class_orientation_count + 1)
        self.assertContains(response=class_orientation_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)








