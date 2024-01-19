from django.urls import path

from topics.views import SubjectsListView, subject_topics

urlpatterns = (
    path('subjects/', SubjectsListView.as_view(), name='subjects-list'),
    path('subject_topics/', subject_topics, name='subject-topics')
)
