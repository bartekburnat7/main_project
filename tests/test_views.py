from django.test import SimpleTestCase
from django.urls import reverse
from fit_sync_app.models import *


class TestViews(SimpleTestCase):

    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def schedule_GET(self):
        response = self.client.get(reverse('schedule'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule.html')
