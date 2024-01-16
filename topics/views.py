from django.shortcuts import render
from django.views.generic import ListView

from topics.models import Subject


class SubjectsListView(ListView):
    model = Subject
    template_name = 'main_pages/after_login_main_page.html'

