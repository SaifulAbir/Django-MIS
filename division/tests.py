from django.test import SimpleTestCase
from django.test import TestCase
from division.models import Division_name


class DivisionTest(SimpleTestCase):

    def test_division_add(self):
        response = self.client.get('/division/division_add/')
        self.assertEqual(response.status_code, 200)

#
# class Division_name_test(TestCase):
#
#     def test_create_divition(self, Division="Dhaka"):
#         return Division.objects.create(Division=Division, )
#
#     def test_Division_creation(self):
#         D = self.create_division()
#         self.assertTrue(isinstance(D, Division))
#         self.assertEqual(D.__unicode__(), D.Division)



class Setup_Class(TestCase):

    def setUp(self):
        self.Division = Division_name.objects.create(Division="Dhaka")

class Division_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = Division_name(data={'Division': "Dhaka",})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_DivisionForm_invalid(self):
        form = Division_name(data={'Division': "Dhaka",})
        self.assertFalse(form.is_valid())



class Division_Views_Test(TestCase):

    def setUp(self):
        self.Division = Division_name.objects.create(Division="Dhaka")


    def test_home_view(self):
        user_login = self.client.login(email="user@mp.com", password="user")
        self.assertTrue(user_login)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_add_user_view(self):
        response = self.client.get("include url for add user view")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "include template name to render the response")

    # Invalid Data
    def test_add_user_invalidform_view(self):
        response = self.client.post()
        self.assertTrue('"error": true' in response.content)

    # Valid Data
    def test_add_admin_form_view(self):
        user_count = Division.objects.count()
        response = self.client.post(data={'Division': "Dhaka",})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Division.objects.count(), user_count+1)
        self.assertTrue('"error": false' in response.content)