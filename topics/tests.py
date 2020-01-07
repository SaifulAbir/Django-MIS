from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from .models import Topics


class TopicTest(TestCase):

    def test__null_name__should_raise_error(self):
        s = Topics(created_date=timezone.now())
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test__uniqe_validation_added(self):
        unique = Topics._meta.get_field('name').unique
        self.assertIn(str(unique),'True')

    def test__max_length_validation_added(self):
        max_length = Topics._meta.get_field('name').max_length
        self.assertEquals(max_length, 128)


