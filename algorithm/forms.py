from django import forms
from .models import RSA, Sezar, Paillier


class RSAForm(forms.ModelForm):

    class Meta:
        model = RSA
        fields = (
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


class PaillierForm(forms.ModelForm):

    class Meta:
        model = Paillier
        fields = (
            'a',
            'b',
        )
