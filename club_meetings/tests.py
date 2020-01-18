from django.core.exceptions import ValidationError
from django.test import Client
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from districts.models import District
from division.models import Division
from.models import ClubMeetings,School,Topics,User

from accounts.models import User
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from.models import ClubMeetings,School,Topics

class ClubMeetingsTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='01712096801')
        user.set_password('12345')
        user.user_type = 5
        user.save()
        self.user = user
        admin_user = User.objects.create(username='01712096805')
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
        s1 = School(name='Mirpur School', school_id=123, division = self.division, district = self.district)
        s1.save()
        self.school = s1
        skleader = SkLeaderProfile(school=self.school, user=self.user, gender='M', student_class='6',
                                   roll=10, mobile='018152045', image='a.png', joining_date=timezone.now())
        skleader.save()
        self.skleader = skleader
        s2 = ClubMeetings(date=timezone.now(), school=self.school, class_room='7', presence_guide_teacher='1',
                         presence_skleader='1', skleader = self.skleader)
        s2.save()
        self.club_m = s2

        s = SkMemberProfile(school=self.school, user=self.user, gender='M', student_class='6',
                            roll=10, mobile='018152045', image='a.png', joining_date=timezone.now())


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

    #view test
    def test_club_meeting_update_page_status_code(self):
        logged_in = self.client.login(username='01712096801', password='12345')
        self.assertTrue(logged_in)
        club_update_response = self.client.get(reverse('club_meetings:club_meeting_update',
                                                              args=(self.club_m.id,)), follow=True)
        self.assertEquals(club_update_response.status_code, 200)
        self.assertTemplateUsed(club_update_response, 'club_meetings/club_meeting_add.html')
        # self.assertContains(response = club_update_response, text='', html=True).

    def test_when__request_for_club_meeting_report_list__should_return_club_meeting_list(self):
        logged_in = self.client.login(username='01712096805', password='12345')
        self.assertTrue(logged_in)
        club_meeting_count = ClubMeetings.objects.count()
        topic = Topics.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        instance = ClubMeetings.objects.create(date=timezone.now(), school=self.school, class_room='7', presence_guide_teacher='1', skleader = self.skleader,
                         presence_skleader='1')
        instance.topics.set(topic)
        instance.attendance.set(user)
        club_meeting_response = self.client.get(reverse('club_meetings:club_meeting_report_list'), follow=True)
        self.assertEqual(ClubMeetings.objects.count(), club_meeting_count + 1)
        self.assertContains(response=club_meeting_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)

    def test__if_required_field_are_given__should_pass(self):
        topic = Topics.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        instance = ClubMeetings.objects.create(school=self.school,class_room='105', skleader = self.skleader)

        instance.topics.set(topic)
        instance.attendance.set(user)
        try:
            instance.full_clean()
        except:
            self.fail()

    def test_when__search_for_club_meeting_report_list__should_return_report_list_page_status_code(self):
        logged_in = self.client.login(username='01712096805', password='12345')
        self.assertTrue(logged_in)
        club_meeting_response = self.client.get(reverse('club_meetings:club_meeting_search_list'), follow=True)
        self.assertEquals(club_meeting_response.status_code, 200)

    def test_when__school_name_is_searched__should_return_respective_club_meeting_list(self):
        logged_in = self.client.login(username='01712096805', password='12345')
        self.assertTrue(logged_in)
        club_meeting_response = self.client.get(reverse('club_meetings:club_meeting_search_list'),
                                                data={'name_contains': 'Mirpur School'}, follow=True)
        self.assertContains(response=club_meeting_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)

    def test_when__division_name_is_searched__should_return_respective_club_meeting_list(self):
        logged_in = self.client.login(username='01712096805', password='12345')
        self.assertTrue(logged_in)
        club_meeting_response = self.client.get(reverse('club_meetings:club_meeting_search_list'),
                                                data={'division_contains': 'Dhaka'}, follow=True)
        self.assertContains(response=club_meeting_response, status_code=200,
                            text='<td>Dhaka</td>', html=True)

    def test_when__district_name_is_searched__should_return_respective_club_meeting_list(self):
        logged_in = self.client.login(username='01712096805', password='12345')
        self.assertTrue(logged_in)
        club_meeting_response = self.client.get(reverse('club_meetings:club_meeting_search_list'),
                                                data={'district_contains': 'Gazipur'}, follow=True)
        self.assertContains(response=club_meeting_response, status_code=200,
                            text='<td>Gazipur</td>', html=True)

    def test_when__all_are_searched__should_return_respective_club_meeting_list(self):
        logged_in = self.client.login(username='01712096805', password='12345')
        self.assertTrue(logged_in)
        club_meeting_response = self.client.get(reverse('club_meetings:club_meeting_search_list'),
                                                data={'name_contains': 'Mirpur School', 'division_contains': 'Dhaka',
                                                      'district_contains': 'Gazipur'}, follow=True)
        self.assertContains(response=club_meeting_response, status_code=200,
                            text='<td>Mirpur School (123)</td>', html=True)