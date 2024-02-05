from django.urls import path, include

from topics.views import SubjectsListView, subject_topics, topic_comments, main_page, CreateNewTopic, CreateNewComment

urlpatterns = (
    path('', main_page, name='main-page'),
    path('subjects/', SubjectsListView.as_view(), name='subjects-list'),
    path('subject_topics/<int:subject_id>/', subject_topics, name='subject-topics'),
    path('topic_comments/<int:topic_id>/', topic_comments, name='topic-comments'),

    path('add_new_topic/<int:subject_id>/<int:user_id>/', CreateNewTopic.as_view(), name='add-new-topic'),
    path('add_new_comment/<int:topic_id>/<int:user_id>/', CreateNewComment.as_view(), name='add-new-comment')
)
