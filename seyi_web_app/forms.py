from django import forms
from django.core import validators
from django.forms import ModelForm
from seyi_web_app.models import Subscribe, Mycv










class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter FullName'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


class SubscribeForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['sc_email']
        is_exists = Subscribe.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError('Email already exist')
    class Meta():
        model = Subscribe
        fields = '__all__'
        widgets = {'sc_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'})}


# class MyCvForm(forms.Form):
#     class Meta:
#         model= Mycv
#         fields= '__all__'
    


