from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Automatically creates a superuser'

    def handle(self, *args, **kwargs):
        if not UserModel.objects.filter(username='admin').exists():
            UserModel.objects.create_superuser(email='student_forum_superuser', password="studentFF123!")
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))