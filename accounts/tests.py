from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserManagerTests(TestCase):
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


class SignUpPageViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/signup")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "phone_number": "+989123456789",
                "first_name": "testname",
                "last_name": "testlastname",
                "email": "testmail@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].phone_number, "+989123456789"
        )
        self.assertEqual(get_user_model().objects.all()[0].first_name, "testname")
        self.assertEqual(get_user_model().objects.all()[0].last_name, "testlastname")
        self.assertEqual(get_user_model().objects.all()[0].email, "testmail@email.com")


class LoginPageViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_login_view_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            phone_number="+989123456789",
            first_name="testname",
            last_name="testlastname",
            password="testpass123",
            email="testmail@email.com",
        )

    def test_login_form(self):
        response = self.client.post(
            reverse("login"),
            {
                "phone_number": "+989123456789",
                "password": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].phone_number, "+989123456789"
        )
        self.assertEqual(get_user_model().objects.all()[0].first_name, "testname")
        self.assertEqual(get_user_model().objects.all()[0].last_name, "testlastname")
        self.assertEqual(get_user_model().objects.all()[0].email, "testmail@email.com")


class LogoutPageViewTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            phone_number="+989123456789",
            first_name="testname",
            last_name="testlastname",
            password="testpass123",
            email="testmail@email.com",
        )

        self.client.post(
            reverse("login"),
            {
                "phone_number": "+989123456789",
                "password": "testpass123",
            },
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.post("/logout")

        self.assertEqual(response.status_code, 302)

    def test_user_is_logged_out(self):
        self.client.post(reverse("logout"))
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
