from django import forms

from notes.models import UserNote


class UserNoteCreateForm(forms.ModelForm):
    class Meta:
        model = UserNote
        fields = '__all__'