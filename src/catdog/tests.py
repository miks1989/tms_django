from django.test import TestCase
from django.urls import reverse


class TestCatDogView(TestCase):

    def test_get(self):
        response = self.client.get(reverse('catdog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='catdog.html')
        self.assertEqual(len(self.client.session['data_for_session'].keys()), 3)

    def test_post_cat(self):
        response = self.client.post(reverse('catdog'),  {'cat': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='pet.html')

    def test_post_error(self):
        with self.assertRaisesMessage(AttributeError, "are you try to hack?"):
            self.client.post(reverse('catdog'),  {'boris': 'true'})





