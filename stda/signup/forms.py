from django import forms

class PhoneVerificationForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    verification_code = forms.CharField(max_length=6)
