from django.contrib import admin

from topics.models import Subject, Topic, Comment


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
