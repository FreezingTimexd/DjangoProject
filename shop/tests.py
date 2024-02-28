from django.test import TestCase
from django.urls import reverse
from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class CustomerListTestCase(LiveServerTestCase):

    def setUp(self):
        self.client.login(username="test1", password="43102Dima")
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.selenium.get('http://127.0.0.1:8000/')
        super(CustomerListTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(CustomerListTestCase, self).tearDown()

    def test_successful_login(self, username="user1", password="43102Dima", next_url=None):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/')
        username_el = self.selenium.find_element(By.ID, "id_username")
        username_el.send_keys(username)
        password_el = self.selenium.find_element(By.ID, "id_password")
        password_el.send_keys(password)
        submit = self.selenium.find_element(By.ID, 'login_btn')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)

    def test_unsuccessful_login(self, username="test7", password="43102Dima", next_url=None):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/')

        username_el = self.selenium.find_element(By.ID, "id_username")
        username_el.send_keys(username)
        password_el = self.selenium.find_element(By.ID, "id_password")
        password_el.send_keys(password)
        submit = self.selenium.find_element(By.ID, 'login_btn')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
