from django.test import TestCase
from django.contrib.auth import get_user_model


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
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
