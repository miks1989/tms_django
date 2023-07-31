from django.test import TestCase, Client
from django.urls import reverse

from catdog.models import AnimalImage


class TestCatDogView(TestCase):
    fixtures = ['data_for_test.json']

    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('catdog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='catdog.html')

    def test_post_cat(self):
        response = self.client.post(reverse('catdog'), {'cat': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='pet.html')
        self.assertEqual(self.client.session['data_for_session']['species'], 'cat')
        self.assertEqual(len(self.client.session['data_for_session'].keys()), 3)
        self.assertEqual(AnimalImage.objects.count(), 25)

    def test_post_error(self):
        with self.assertRaisesMessage(AttributeError, "are you try to hack?"):
            self.client.post(reverse('catdog'), {'boris': 'true'})

    def test_save_catdog(self):
        data_for_session = {'url': 'test@url',
                            'species': 'cat',
                            'type': 'jpg'}
        session = self.client.session
        session['data_for_session'] = data_for_session
        session.save()
        # self.client.post(reverse('catdog'), {'cat': 'true'}) #если не формируем сами сессию
        responce = self.client.post(reverse('save_catdog'), {'cat': 'true'})
        self.assertEqual(AnimalImage.objects.count(), 26)
        data = AnimalImage.objects.last()
        self.assertEqual(data.url, 'test@url')
        self.assertEqual(data.species, 'cat')
        self.assertEqual(data.type, 'jpg')
        self.assertTemplateUsed(responce, template_name='petsaved.html')
