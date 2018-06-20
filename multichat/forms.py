from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    @property
    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
                level =0
            )


class LoginForm(forms.ModelForm):
    def __init__( self, *args, **kwargs ):
        super( LoginForm, self ).__init__( *args, **kwargs )
        self.field[ 'my_field' ].widget.attrs.update( {
            'class': 'form-control',
            'placeholder': 'Do not use numbers.' } )

    class Meta:
        model = User
        fields = ['username', 'password']


