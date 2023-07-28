from django import forms
from newest.models import student


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'admission', 'course']
