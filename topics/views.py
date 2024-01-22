from django.shortcuts import render
from django.views.generic import ListView

from topics.models import Subject, Topic, Comment


class SubjectsListView(ListView):
    model = Subject
    template_name = 'main_pages/after_login_main_page.html'


def subject_topics(request, subject_id):

    current_subject_topics = Topic.objects.filter(subject_id=subject_id)

    context = {
        'topics': current_subject_topics,
    }

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