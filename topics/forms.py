from django import forms
from .models import Topics
import topics.strings as topic_strings



class TopicsForm(forms.ModelForm):
    name = forms.CharField(label=topic_strings.TOPIC_NAME)
    class Meta:
        model = Topics
        fields = ['name']
        widgets = {
            'name': forms.TextInput(),
        }