from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from rest_framework.authtoken.models import Token

from accounts.factories import UserFactory
from heroes.factories import HeroFactory


class HeroViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.API_LIMIT = settings.REST_FRAMEWORK['PAGE_SIZE']
        self.user_factory = UserFactory()

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

    def test_create_new_hero(self):
        url = reverse('api:heroes:list')

        hero_data = {
            'name': 'Super Baddie',
            'alignment': 'good',
            'gender': 'female',
            'power': 'painter'
        }
        token = Token.objects.create(user=self.user_factory)
        response = self.client.post(url, hero_data,
                                    HTTP_AUTHORIZATION=f'Token {token}',
                                    content_type='application/json')
        self.assertContains(response, 'Super Baddie', status_code=201)

    def test_update_hero(self):
        hero = HeroFactory()
        url = reverse('api:heroes:detail', args=[hero.uuid])

        hero_data = {'alignment': 'bad'}
        token = Token.objects.create(user=self.user_factory)
        response = self.client.patch(url, hero_data,
                                     HTTP_AUTHORIZATION=f'Token {token}',
                                     content_type='application/json')
        self.assertContains(response, hero.name, status_code=200)
