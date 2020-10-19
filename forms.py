from django import forms
from .models import Izdano

class IzdanoForm(forms.ModelForm):
    class Meta:
        model = Izdano
        fields = "__all__"
