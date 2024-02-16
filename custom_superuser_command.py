import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Student_Forum_Bulgaria.settings")
django.setup()

from django.contrib.auth import get_user_model

UserModel = get_user_model()

if not UserModel.objects.filter(email='student_forum_superuser@hotmail.com').exists():
    UserModel.objects.create_superuser(email='student_forum_superuser@hotmail.com', password="studentFF123!")
