import csv

from os.path import join as join_paths

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from heroes.models import Hero


class Command(BaseCommand):
    help = 'Adds base heroes to app from CSV assets.'

    def handle(self, *args, **options):
        hero_info_path = join_paths(settings.ASSETS_PATH, 'characters_info.csv')
        hero_stats_path = join_paths(settings.ASSETS_PATH, 'characters_stats.csv')
        info_fields = ['id', 'name', 'alignment', 'gender', 'eye_color', 'race', 'hair_color',
                       'publisher', 'skin_color', 'height', 'weight']
        stat_fields = ['name', 'alignment', 'intelligence', 'strength',
                       'speed', 'durability', 'power', 'combat', 'total']

        def update_hero(hero):
            # TODO: Do checks for dirty field values like empty strings, dashes
            if 'id' in hero.keys():
                hero.pop('id')
            if 'total' in hero.keys():
                hero.pop('total')
            exists = Hero.objects.filter(name=hero['name']).update(**hero)
            if exists:
                return Hero.objects.filter(name=hero['name']).first()
            return Hero.objects.update_or_create(**hero)

        try:
            with open(hero_info_path) as file:
                heroes_data = csv.DictReader(file, fieldnames=info_fields)

                heroes = list(map(update_hero, heroes_data))

                self.stdout.write(self.style.SUCCESS(f'Successfully created {len(heroes)} heroes'))

            with open(hero_stats_path) as file:
                heroes_data = csv.DictReader(file, fieldnames=stat_fields)
                heroes = list(map(update_hero, heroes_data))

                self.stdout.write(self.style.SUCCESS(f'Successfully updated {len(heroes)} heroes'))
        except (CommandError, TypeError, ValueError, KeyError) as exc:
            raise exc
