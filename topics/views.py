from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView

from topics.forms import AddNewTopicForm
from topics.models import Subject, Topic, Comment

import re

UserModel = get_user_model()


class SubjectsListView(ListView):
    model = Subject
    template_name = 'main_pages/after_login_main_page.html'


def main_page(request):
    return render(request, 'main_pages/main_page.html')


def subject_topics(request, subject_id):

    current_subject_topics = Topic.objects.filter(subject_id=subject_id)

    context = {
        'subject_id': subject_id,
        'topics': current_subject_topics,
    }

    print(request.user.id)

    for topic in current_subject_topics:
        print(topic.user.profileuser.first_name, topic.user.profileuser.last_name)

    return render(request, 'main_pages/subject_topics.html', context=context)


def topic_comments(request, topic_id):

    curr_topic = Topic.objects.get(id=topic_id)
    current_topic_comments = Comment.objects.filter(topic_id=topic_id)

    context = {
        'topic': curr_topic,
        'comments': current_topic_comments,
    }

    print(curr_topic.user.profileuser.first_name, curr_topic.user.profileuser.last_name)

    return render(request, 'main_pages/topics_comments_page.html', context=context)


class CreateNewTopic(CreateView):

    template_name = 'main_pages/add_new_topic.html'
    form_class = AddNewTopicForm
    success_url = reverse_lazy('subject-topics')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        matched_subject_id = re.findall(r'\d$', str(self.request.META['HTTP_REFERER']))
        print(int(matched_subject_id[0]))

        context['subject_id'] = int(matched_subject_id[0])

        return context
