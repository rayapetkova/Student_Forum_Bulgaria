from django import forms

from topics.models import Topic


class AddNewTopicForm(forms.ModelForm):

    description = forms.Textarea()

    class Meta:
        model = Topic
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'topic-name'
        self.fields['description'].widget.attrs['class'] = 'topic-description'


