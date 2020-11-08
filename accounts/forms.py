from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm


class AccountCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']


class AccountUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']


class AccountEdinPasswordForm(PasswordChangeForm):
    pass
