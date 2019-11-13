from django import forms
from .models import Number

"""simple form with given_number field"""


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ('given_number',)
