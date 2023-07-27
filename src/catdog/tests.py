from django.test import TestCase
from django.urls import reverse

class TestCatDogView(TestCase):

    def test_get(self):
        request = self.client.get(reverse('catdog'))
        self.assertTemplateUsed(template_name='catdog.html')
