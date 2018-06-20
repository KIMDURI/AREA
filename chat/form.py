from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        #field = ['salutation', 'first_name', 'last_name', 'email']
