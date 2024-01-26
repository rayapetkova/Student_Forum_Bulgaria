from django.urls import path

from topics.views import SubjectsListView, subject_topics, topic_comments, main_page

urlpatterns = (
    path('', main_page, name='main-page'),
    path('subjects/', SubjectsListView.as_view(), name='subjects-list'),
    path('subject_topics/<int:subject_id>', subject_topics, name='subject-topics'),
    path('topic_comments/<int:topic_id>', topic_comments, name='topic-comments')
)
