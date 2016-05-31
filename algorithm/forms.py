from django import forms
from .models import RSA, Sezar


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


class SezarForm(forms.ModelForm):

    class Meta:
        model = Sezar
        fields = (
            'a',
            'b',
            'k',
        )
