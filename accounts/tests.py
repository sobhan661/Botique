from django.test import TestCase
from django.contrib.auth import get_user_model


from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            phone_number="+989123456789",
            first_name="testname",
            last_name="testlastname",
            password="testpass123",
            email="testmail@email.com",
        )

        self.assertEqual(user.phone_number, "+989123456789")
        self.assertEqual(user.first_name, "testname")
        self.assertEqual(user.last_name, "testlastname")
        self.assertEqual(user.email, "testmail@email.com")

        self.assertTrue(user.is_active)
        self.assertTrue(user.check_password("testpass123"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            phone_number="+989123456789",
            first_name="testname",
            last_name="testlastname",
            password="testpass123",
            email="testmail@email.com",
        )

        self.assertEqual(user.phone_number, "+989123456789")
        self.assertEqual(user.first_name, "testname")
        self.assertEqual(user.last_name, "testlastname")
        self.assertEqual(user.email, "testmail@email.com")

        self.assertTrue(user.is_active)
        self.assertTrue(user.check_password("testpass123"))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class UserCreationFormTests(TestCase):
    def test_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(
            data={
                "phone_number": "+989123456789",
                "first_name": "testname",
                "last_name": "testlastname",
                "email": "testmail@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            }
        )

        self.assertTrue(form.is_valid())
        user = form.save()

        self.assertEqual(user.phone_number, "+989123456789")
        self.assertEqual(user.first_name, "testname")
        self.assertEqual(user.last_name, "testlastname")
        self.assertEqual(user.email, "testmail@email.com")

        self.assertTrue(user.check_password("testpass123"))


class UserChangeFormTests(TestCase):
    def setup(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            phone_number="+989123456789",
            first_name="testname",
            last_name="testlastname",
            password="testpass123",
            email="testmail@email.com",
        )

    def test_user_creation_form_valid_data(self):
        form = CustomUserChangeForm(
            data={
                # "phone_number": "+989123456789",
                "first_name": "testname",
                "last_name": "testlastname",
                "email": "testmail@email.com",
                "is_active": True,
            },
        )

        self.assertTrue(form.is_valid())
        user = form.save()

        # self.assertEqual(user.phone_number, "+989123456789")
        self.assertEqual(user.first_name, "testname")
        self.assertEqual(user.last_name, "testlastname")
        self.assertEqual(user.email, "testmail@email.com")

        # self.assertTrue(user.check_password("testpass123"))
