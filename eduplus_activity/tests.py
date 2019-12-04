from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from accounts.models import User
from eduplus_activity.models import EduPlusActivity
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
        s1 = School(name='Mirpur School', school_id=123)
        s1.save()
        self.school = s1
        # s2 = ClubMeetings(date=timezone.now(), school=self.school, class_room='7', presence_guide_teacher='1',
        #                  presence_skleader='1')
        # s2.save()
        # self.club_m = s2
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
    #
    # #view test
    # def test_club_meeting_update_page_status_code(self):
    #     logged_in = self.client.login(email='test@example.com', password='12345')
    #     self.assertTrue(logged_in)
    #     club_update_response = self.client.get(reverse('club_meetings:club_meeting_update',
    #                                                           args=(self.club_m.id,)), follow=True)
    #     self.assertEquals(club_update_response.status_code, 200)
    #     self.assertTemplateUsed(club_update_response, 'club_meetings/club_meeting_add.html')
    #     # self.assertContains(response = club_update_response, text='', html=True).

    def test__if_required_data_is_given__should_pass(self):
        topic = Topics.objects.exclude(name='')
        user = User.objects.filter(user_type='6')
        instance = EduPlusActivity.objects.create(date=timezone.now(), school=self.school,presence_skleader=True, description='Nothing done')

        instance.topics.set(topic)
        instance.attendance.set(user)
        try:
            instance.full_clean()
        except:
            self.fail()
