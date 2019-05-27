from django.test import TestCase
from django.urls import reverse, resolve

from accounts.factories import User, UserFactory
from heroes.factories import HeroFactory


class HeroViewsTestCase(TestCase):
    def test_get_all_heroes(self):
        url = reverse('api:heroes:list')
        hero = HeroFactory(name='Super Hero')

        response = self.client.get(url)
        self.assertContains(response, hero.uuid, status_code=200)

    def test_get_hero_detail(self):
        hero = HeroFactory(name='Super Hero')
        url = reverse('api:heroes:detail', args=[hero.uuid])

        response = self.client.get(url)
        self.assertContains(response, hero.name, status_code=200)

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
