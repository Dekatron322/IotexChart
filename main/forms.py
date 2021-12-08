from django import forms
from django.forms.widgets import DateInput, TextInput

from .models import *




class UnvettedForm(forms.ModelForm):
    token_address = models.CharField(max_length=120)
    telegram_url = models.CharField(max_length=120)
    #proof_of_payment = models.CharField(max_length=200)
    image = models.ImageField()


    class Meta():
        model = Unvetted
        fields = ("token_address", "telegram_url", "image")

class VerifyVettedForm(forms.ModelForm):
    status = models.BooleanField(default=False)
    class Meta():
        model = Unvetted
        fields = ["status"]


class BannerForm(forms.ModelForm):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    image = models.ImageField()

    interest = models.CharField(max_length=200)
    budget = models.CharField(max_length=100)
    proof_of_payment = models.CharField(max_length=100)
    about_project = models.TextField()


    class Meta():
        model = Banner
        fields = ("title", "text", "link", "company_name", "image", "interest", "budget", "proof_of_payment", "about_project")


class VerifyBannerForm(forms.ModelForm):
    status = models.BooleanField(default=False)
    class Meta():
        model = Banner
        fields = ["status"]



