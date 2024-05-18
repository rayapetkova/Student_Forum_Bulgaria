from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView

from topics.forms import AddNewTopicForm, AddNewCommentForm, AddNewSubjectForm
from topics.models import Subject, Topic, Comment

import re

UserModel = get_user_model()


class SubjectsListView(ListView):
    model = Subject
    template_name = 'main_pages/after_login_main_page.html'


def main_page(request):
    return render(request, 'main_pages/main_page.html')


def subject_topics(request, subject_id):
    # Get the topics in descending order by the id (the last added topic is the first one)
    current_subject_topics = Topic.objects.filter(subject_id=subject_id).order_by('-id')

    context = {
        'subject_id': subject_id,
        'topics': current_subject_topics,
    }

    print(request.user.id)

    for topic in current_subject_topics:
        print(topic.user.profileuser.first_name, topic.user.profileuser.last_name)

    return render(request, 'main_pages/subject_topics.html', context=context)


@login_required
def topic_comments(request, topic_id):

    curr_topic = Topic.objects.get(id=topic_id)
    # Get the comments in descending order by the id (the last added comment is the first one)
    current_topic_comments = Comment.objects.filter(topic_id=topic_id).order_by('-id')

    context = {
        'topic': curr_topic,
        'comments': current_topic_comments,
    }

    print(curr_topic.user.profileuser.first_name, curr_topic.user.profileuser.last_name)

    return render(request, 'main_pages/topics_comments_page.html', context=context)


class CreateNewSubject(CreateView):

    template_name = 'main_pages/add_new_subject.html'
    form_class = AddNewSubjectForm
    success_url = reverse_lazy('subjects-list')


class CreateNewTopic(CreateView):

    template_name = 'main_pages/add_new_topic.html'
    form_class = AddNewTopicForm

    # When the user successfully creates a comment he is redirected to a success page
    def get_success_url(self):
        return reverse_lazy('subject-topics', kwargs={'subject_id': self.kwargs['subject_id']})

    # Add context that can be used in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # print(str(self.request.META['HTTP_REFERER']))
        # matched_subject_id = re.findall(r'\d{1,}\/$', str(self.request.META['HTTP_REFERER']))
        # print(int(matched_subject_id[0][:-1]))

        subject_id = self.kwargs['subject_id']

        subject = Subject.objects.get(id=subject_id)

        context['subject_id'] = subject_id
        context['subject_name'] = subject.name

        return context

    # Check if the form is valid and set subject_id and user_id to the form instance
    def form_valid(self, form):
        subject_id = self.kwargs['subject_id']
        user_id = self.kwargs['user_id']

        form.instance.subject_id = subject_id
        form.instance.user_id = user_id
        
        return super().form_valid(form)


class CreateNewComment(CreateView):

    template_name = 'main_pages/add_new_comment.html'
    form_class = AddNewCommentForm

    # When the user successfully creates a comment he is redirected to a success page
    def get_success_url(self):
        return reverse_lazy('topic-comments', kwargs={'topic_id': self.kwargs['topic_id']})

    # Add context that can be used in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # matched_topic_id = re.findall(r'\d{1,}\/$', str(self.request.META['HTTP_REFERER']))
        # topic_id = int(matched_topic_id[0][:-1])

        topic_id = self.kwargs['topic_id']
        topic = Topic.objects.get(id=topic_id)

        context['topic_id'] = topic.id
        context['topic_name'] = topic.name
        context['topic_description'] = topic.description
        context['subject_name'] = topic.subject.name

        return context

    # Check if the form is valid and set topic_id and user_id to the form instance
    def form_valid(self, form):
        topic_id = self.kwargs['topic_id']
        user_id = self.kwargs['user_id']

        form.instance.topic_id = topic_id
        form.instance.user_id = user_id

        return super().form_valid(form)
