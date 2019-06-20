import random

from django.core.management.base import BaseCommand, CommandError

from heroes.models import Hero


class Command(BaseCommand):
    help = 'Generates base hero stats and attributes randomly.'

    def handle(self, *args, **options):
        attr_fields = ['height', 'weight', 'alignment', 'intelligence',
                       'strength', 'speed', 'durability', 'power', 'combat']
        heroes = Hero.objects.all()

        def update_stat(hero):
            for attr in attr_fields:
                current = getattr(hero, attr)
                if not current or current == '-':
                    value = random.randrange(25, 100)
                    setattr(hero, attr, str(value))
            hero.save()
            return hero

        results = list(map(update_stat, heroes))

        self.stdout.write(self.style.SUCCESS(f'{len(results)} hero stats updated.'))
