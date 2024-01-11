from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UsernameField
from django import forms

from accounts_users.models import ProfileUser
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=commit)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        user_profile = ProfileUser(
            first_name=first_name,
            last_name=last_name,
            user=user
        )

        if commit:
            user_profile.save()

        return user
