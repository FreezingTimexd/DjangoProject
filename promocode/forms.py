from django import forms


class PromocodeApplyForm(forms.Form):
    code = forms.CharField()
