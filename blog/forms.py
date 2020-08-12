from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget


class ArticleForm(forms.ModelForm):
    """Form for creating an article"""
    forms.CharField(widget=CKEditorWidget, label='')

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {'created_date': forms.HiddenInput}