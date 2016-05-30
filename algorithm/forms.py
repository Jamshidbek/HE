from django import forms
from .models import RSA


class RSAForm(forms.ModelForm):

    class Meta:
        model = RSA
        fields = (
            'p',
            'q',
            'e',
            'a1',
            'b1',
        )
