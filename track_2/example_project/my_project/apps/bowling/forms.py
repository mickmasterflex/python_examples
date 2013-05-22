from django import forms
from django.contrib.auth.models import User

class Score(forms.ModelForm):
    """
    Defines the form for the user My Account area.
    """
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    score = forms.IntegerField(max_length=3, required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'score',
        )
