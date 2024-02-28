from django.contrib.auth.models import User
import factory
from django.test import TestCase


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserTestCase(TestCase):
    def setUp(self):
        self.test_user = UserFactory.create(
            password='12345t',
            username='test_user',
            email='test_user@gmail.com',
            first_name='test_first',
            last_name='test_last')

    def test_user_created(self):
        self.assertEqual(self.test_user.password, '12345t')
        self.assertEqual(self.test_user.username, 'test_user')
        self.assertEqual(self.test_user.email, 'test_user@gmail.com')
        self.assertEqual(self.test_user.first_name, 'test_first')
        self.assertEqual(self.test_user.last_name, 'test_last')
