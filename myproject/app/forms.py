from django import forms
from app.models import Course

class LessonForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(), label='Nomi', required=False)
    content = forms.CharField(widget=forms.Textarea(), label='Contenti', required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(), label="Kursi", required=False)