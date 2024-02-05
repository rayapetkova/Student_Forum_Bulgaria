from django import forms

from topics.models import Topic, Comment, Subject


class AddNewSubjectForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Subject
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'subject-name'
        self.fields['description'].widget.attrs['class'] = 'subject-description'


class AddNewTopicForm(forms.ModelForm):

    description = forms.Textarea()

    class Meta:
        model = Topic
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'topic-name'
        self.fields['description'].widget.attrs['class'] = 'topic-description'


class AddNewCommentForm(forms.ModelForm):

    comment_text = forms.CharField(widget=forms.Textarea)
    # comment_text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment_text'].widget.attrs['class'] = 'comment-text'
