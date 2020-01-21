from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from events.models import Event


class EventTests(TestCase):

    ## Event title testing start
    def test__null_title__should_raise_error(self):
        event = Event(start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=2))
        with self.assertRaises(ValidationError):
            event.full_clean()

    def test__empty_title__should_raise_error(self):
        event = Event(title='', start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=2))
        with self.assertRaises(ValidationError):
            event.full_clean()

    def test__128_plus_char_title__should_raise_error(self):
        event = Event(
            title="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam nulla porttitor massa id neque aliquam.",
            start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=2))
        with self.assertRaises(ValidationError):
            event.full_clean()

    def test__dash_in_title__should_pass(self):
        event = Event(title='AA-', start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=2))
        try:
            event.full_clean()
        except:
            self.fail()

    ## Event date testing start
    def test__if_end_date_before_start_date__should_raise_error(self):
        event = Event(
            title="test", start_date=timezone.now(), end_date=timezone.now() - timezone.timedelta(days=2))
        with self.assertRaises(ValidationError):
            event.full_clean()
    def test__if_end_date_before_start_date__should__pass(self):
        event = Event(
            title="test", start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=2))
        try:
            event.full_clean()
        except:
            self.fail()

    def test__start_date_null_validation_added(self):
        null = Event._meta.get_field('start_date').null
        self.assertEquals(null, False)

    def test__end_date_null_validation_added(self):
        null = Event._meta.get_field('end_date').null
        self.assertEquals(null, False)
