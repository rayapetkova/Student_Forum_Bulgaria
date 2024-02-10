from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from accounts_users.models import ProfileUser
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-input-fields'
        self.fields['password'].widget.attrs['class'] = 'form-input-fields'


class RegisterUserForm(auth_forms.UserCreationForm):

    ROLE_CHOICES = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('External User', 'External User')
    )

    first_name = forms.CharField()
    last_name = forms.CharField()

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES
    )

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-input-fields'
        self.fields['last_name'].widget.attrs['class'] = 'form-input-fields'
        self.fields['email'].widget.attrs['class'] = 'form-input-fields'
        self.fields['password1'].widget.attrs['class'] = 'form-input-fields'
        self.fields['password2'].widget.attrs['class'] = 'form-input-fields'
        self.fields['role'].widget.attrs['class'] = 'form-input-role'
    
    def save(self, commit=True):
        user = super().save(commit=commit)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        role = self.cleaned_data['role']

        user_profile = ProfileUser(
            first_name=first_name,
            last_name=last_name,
            role=role,
            user=user
        )

        if commit:
            user_profile.save()

        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileUser
        fields = ('first_name', 'last_name', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-input-fields'
        self.fields['last_name'].widget.attrs['class'] = 'form-input-fields'
        self.fields['role'].widget.attrs['class'] = 'form-input-role'