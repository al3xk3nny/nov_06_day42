from django import forms
from .models import Topic
from .models import Book

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields = "__all__"
