import jwt
from secrets import token_urlsafe

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from accounts.models import User


class Command(BaseCommand):
    help = 'Adds or resets student user secret key.'

    def add_arguments(self, parser):
        parser.add_argument('--secret', dest='api_secret', nargs='+')

    def handle(self, *args, **options):
        student, _ = User.objects.get_or_create(username='studentdev',
                                                email='studentdev@herobookapi.com')
        student.set_password('imahero')
        student.first_name = 'Student'
        student.last_name = 'Dev'
        token = token_urlsafe(32)
        student.api_secret = options.get('api_secret', token)
        student.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully updated student user.'))
