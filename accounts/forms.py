from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    conferm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))



    class Meta:
        model    = Account
        fields   = ['first_name','last_name','phone_number','email','password']

    def __init__(self,  *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder','required'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder','required'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder','required'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder','required'] = 'Enter Email'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        conferm_password = cleaned_data.get("conferm_password")

        if password != conferm_password:
            raise forms.ValidationError(
                'Password Does not Match!'
            )
        
        