from django import forms
from django.contrib.auth.models import User

from accounts import utils
from accounts import constants


class MyUserForm(forms.ModelForm):
    """
    Defines the form for the user My Account area.
    """
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class UserForm(MyUserForm):
    """
    Defines the form for the generic user.
    """
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    access_level = forms.ChoiceField(choices=constants.PERMISSION_CHOICES)

    class Meta(MyUserForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_username(self):
        username = self.data['username']
        if utils.is_username_valid(username) or\
                self.instance.username == username:
            return username
        else:
            raise forms.ValidationError('The username "{0}" is already '
                    'taken'.format(username))

    def save(self, commit=True):
        user = super(UserForm, self).save()

        profile = user.profile
        profile.permission = self.cleaned_data['access_level']
        profile.save()

        return user
