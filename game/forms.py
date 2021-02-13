from django import forms
from django.forms import ModelForm

from .models import Quarterback, Runningback, Widereceiver, Tightend, Kicker, Team



class Quarterbackform(forms.ModelForm):  
    class Meta:  
        model = Quarterback 
        fields = ('name',) 
        labels = { 'name': ('')}
        widgets = {
        'name': forms.TextInput(attrs={
            'id':'QB_name',
            'class': 'form-control',
            'placeholder': 'Quarterback'
            })
        }

class Runningbackform(forms.ModelForm):  
    class Meta:  
        model = Runningback  
        fields = ('name',) 
        labels = { 'name': ('')} 
        widgets = {
        'name': forms.TextInput(attrs={
            'id':'RB_name',
            'class': 'form-control',
            'placeholder': 'Running Back'})
        }

class Widereceiverform(forms.ModelForm):  
    class Meta:  
        model = Widereceiver  
        fields = ('name',) 
        labels = { 'name': ('')}
        widgets = {
        'name': forms.TextInput(attrs={
            'id':'WR_name',
            'class': 'form-control',
            'placeholder': 'Wide Receiver'})
        }  

class Tightendform(forms.ModelForm):  
    class Meta:  
        model = Tightend 
        fields = ('name',) 
        labels = { 'name': ('')}
        widgets = {
        'name': forms.TextInput(attrs={
            'id':'TE_name',
            'class': 'form-control',
            'placeholder': 'Tightend'})
        }  

class Kickerform(forms.ModelForm):  
    class Meta:  
        model = Kicker  
        fields = ('name',) 
        labels = { 'name': ('')}
        widgets = {
        'name': forms.TextInput(attrs={
            'id':'K_name',
            'class': 'form-control',
            'placeholder': 'Kicker'})
        }  

class Teamform(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name',)
        