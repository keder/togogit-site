from django import forms

from usernotes.models import UserNote


class UserNoteCreateForm(forms.ModelForm):
    class Meta:
        model = UserNote
        fields = '__all__'