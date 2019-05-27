from unittest import skip

from django.conf import settings
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.factories import User, UserFactory
from heroes.factories import HeroFactory


class HeroViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.API_LIMIT = settings.REST_FRAMEWORK['PAGE_SIZE']

    def test_get_all_heroes(self):
        url = reverse('api:heroes:list')
        hero = HeroFactory(name='Super Hero')

        response = self.client.get(url)
        self.assertContains(response, hero.uuid, status_code=200)
        self.assertLessEqual(len(response.data['results']), self.API_LIMIT)

    def test_create_heroes_fails_without_auth(self):
        url = reverse('api:heroes:list')
        hero_data = {
            'name': 'Super Baddie',
            'alignment': 'good',
            'gender': 'female',
            'power': 'painter'
        }

        response = self.client.post(url, hero_data)
        self.assertEqual(response.status_code, 401)

    def test_get_hero_detail(self):
        hero = HeroFactory(name='Super Hero')
        url = reverse('api:heroes:detail', args=[hero.uuid])

        response = self.client.get(url)
        self.assertContains(response, hero.name, status_code=200)

    @skip('To implement with 1.1 dev api auth')
    def test_create_new_hero(self):
        # user = UserFactory(name='testuser', email='testuser@example.co',
        #                    password='password')
        user = User.objects.create_user('testuser', email='test@ex.co', password='secretz107')
        url = reverse('api:heroes:list')

        hero_data = {
            'name': 'Super Baddie',
            'alignment': 'good',
            'gender': 'female',
            'power': 'painter'
        }
        user = {'username': user.username,
                'password': user.password}
        auth = self.client.post('/authorize/', user)
        response = self.client.post(url, hero_data,
                                    headers={'Authorization': auth['token']},
                                    content_type='application/json')
        self.assertContains(response, 'Super Baddie', status_code=201)
