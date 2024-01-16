from django.urls import path

from topics.views import SubjectsListView

urlpatterns = (
    path('subjects/', SubjectsListView.as_view(), name='subjects-list'),
)
