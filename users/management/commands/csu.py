from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='serj@sky.pro',
            first_name='Sergei',
            last_name='Valdemarov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456')
        user.save()