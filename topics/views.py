from django.shortcuts import render
from django.views.generic import ListView

from topics.models import Subject


class SubjectsListView(ListView):
    model = Subject
    template_name = 'main_pages/after_login_main_page.html'


def subject_topics(request):
    return render(request, 'main_pages/subject_topics.html')