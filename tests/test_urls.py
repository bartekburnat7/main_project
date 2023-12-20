from django.test import SimpleTestCase
from django.urls import reverse, resolve
from fit_sync_app.views import *


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('home')
        print(url)
        self.assertEqual(resolve(url).func, index)

    def test_features_url_is_resolved(self):
        url = reverse('features')
        print(url)
        self.assertEqual(resolve(url).func, features)

    def test_goals_url_is_resolved(self):
        url = reverse('goals')
        print(url)
        self.assertEqual(resolve(url).func, goals)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        print(url)
        self.assertEqual(resolve(url).func, about)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        print(url)
        self.assertEqual(resolve(url).func, dashboard)

    def test_student_dashboard_url_is_resolved(self):
        url = reverse('student_dashboard')
        print(url)
        self.assertEqual(resolve(url).func, student_dashboard)

    def test_schedule_url_is_resolved(self):
        url = reverse('schedule')
        print(url)
        self.assertEqual(resolve(url).func, schedule)

    def test_delete_lesson_url_is_resolved(self):
        url = reverse('delete_lesson', args=['10'])
        print(url)
        self.assertEqual(resolve(url).func, DeleteLesson)

    def test_edit_lesson_url_is_resolved(self):
        url = reverse('edit_lesson', args=['10'])
        print(url)
        self.assertEqual(resolve(url).func, EditLesson)

    def test_accept_lesson_url_is_resolved(self):
        url = reverse('accept_lesson', args=['10'])
        print(url)
        self.assertEqual(resolve(url).func, AcceptLesson)

    def test_cancel_lesson_url_is_resolved(self):
        url = reverse('cancel_lesson', args=['10'])
        print(url)
        self.assertEqual(resolve(url).func, CancelLesson)
