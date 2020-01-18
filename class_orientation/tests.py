from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from districts.models import District
from division.models import Division
from skleaders.models import SkLeaderProfile
from topics.models import Topics
from.models import PeerEducation,School

class ClassOrientationTest(TestCase):

    def setUp(self):
        user = User.objects.create(email='test@example.com', username='01712062778')
        user.set_password('12345')
        user.user_type = 5
        user.save()
        self.user = user
        admin_user = User.objects.create(email='admin@example.com', username='01712062768')
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
        skleader = SkLeaderProfile(school=self.school, user=self.user, gender='M', student_class='6',
                                   roll=10, mobile='018152045', image='a.png', joining_date=timezone.now())
        skleader.save()
        to = Topics.objects.all()
        co = PeerEducation.objects.create(created_date=timezone.now(), place='1', school=self.school)
        co.topic.set(to)
        self.peer_education = co

    def test__when_school_is_null__should_raise_error(self):
        s = PeerEducation(created_date=timezone.now(), place='1', )
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__when_place_is_null__should_raise_error(self):
        s = PeerEducation(created_date=timezone.now(), place='', school=self.school, )
        with self.assertRaises(ValidationError):
            s.full_clean()

    # view test
    def test_peer_education_add_page_status_code_content_type(self):
        logged_in = self.client.login(username='01712062778', password='12345')
        self.assertTrue(logged_in)
        orientation_add_response = self.client.get('/peer_education/add/', follow=True)
        self.assertEquals(orientation_add_response.status_code, 200)
        self.assertEquals(orientation_add_response['Content-Type'], 'application/json')

    def test_peer_education_update_page_status_code_content_type(self):
        logged_in = self.client.login(username='01712062778', password='12345')
        self.assertTrue(logged_in)
        orientation_update_response = self.client.get(reverse('peer_education:peer_education_update',
                                                              args=(self.peer_education.id,)), follow=True)
        self.assertEquals(orientation_update_response.status_code, 200)
        self.assertEquals(orientation_update_response['Content-Type'], 'application/json')

    def test_when__request_for_peer_education_report_list__should_return_peer_education_list(self):
        logged_in = self.client.login(username='01712062768', password='12345')
        self.assertTrue(logged_in)
        peer_education_count = PeerEducation.objects.count()
        topic = Topics.objects.exclude(name='')
        instance = PeerEducation.objects.create(created_date=timezone.now(), place='1', school=self.school)
        instance.topic.set(topic)
        peer_education_response = self.client.get(reverse('peer_education:peer_education_report_list'), follow=True)
        self.assertEqual(PeerEducation.objects.count(), peer_education_count + 1)
        self.assertContains(response=peer_education_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)

    def test_when__search_for_peer_education_report_list__should_return_report_list_page_status_code(self):
        logged_in = self.client.login(username='01712062768', password='12345')
        self.assertTrue(logged_in)
        peer_education_response = self.client.get(reverse('peer_education:peer_education_search_list'), follow=True)
        self.assertEquals(peer_education_response.status_code, 200)

    def test_when__school_name_is_searched__should_return_respective_peer_education_list(self):
        logged_in = self.client.login(username='01712062768', password='12345')
        self.assertTrue(logged_in)
        peer_education_response = self.client.get(reverse('peer_education:peer_education_search_list'),
                                                data={'name_contains': 'Mirpur School'}, follow=True)
        self.assertContains(response=peer_education_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)

    def test_when__division_name_is_searched__should_return_respective_peer_education_list(self):
        logged_in = self.client.login(username='01712062768', password='12345')
        self.assertTrue(logged_in)
        peer_education_response = self.client.get(reverse('peer_education:peer_education_search_list'),
                                                data={'division_contains': 'Dhaka'}, follow=True)
        self.assertContains(response=peer_education_response, status_code=200,
                            text='<td>Dhaka</td>', html=True)

    def test_when__district_name_is_searched__should_return_respective_peer_education_list(self):
        logged_in = self.client.login(username='01712062768', password='12345')
        self.assertTrue(logged_in)
        peer_education_response = self.client.get(reverse('peer_education:peer_education_search_list'),
                                                data={'district_contains': 'Gazipur'}, follow=True)
        self.assertContains(response=peer_education_response, status_code=200,
                            text='<td>Gazipur</td>', html=True)

    def test_when__all_are_searched__should_return_respective_peer_education_list(self):
        logged_in = self.client.login(username='01712062768', password='12345')
        self.assertTrue(logged_in)
        peer_education_response = self.client.get(reverse('peer_education:peer_education_search_list'),
                                                data={'name_contains': 'Mirpur School', 'division_contains': 'Dhaka',
                                                      'district_contains': 'Gazipur'}, follow=True)
        self.assertContains(response=peer_education_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)








