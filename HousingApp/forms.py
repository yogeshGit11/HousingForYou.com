from django import forms
from .models import HouseOnRent,HouseOnSell
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class PublishHouseOnRentForm(forms.ModelForm):
    class Meta:
        model=HouseOnRent
        fields=['house_photos','house_type','about_house','house_location','city_name','Owner_name','contact_number','house_rent']
        labels={'house_photos':'Add Photo'}


    about_house=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control border border-dark mt-2','placeholder':'Write Something About this house...',"rows":"7"}),label='')

    house_location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'Location of house'}),label='')

    city_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'City'}),label='')

    Owner_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'Name Of Owner'}),label='')

    contact_number=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control border border-dark','placeholder':'Contcat number of owner'}),label='',error_messages={'max_length':'Please Enter the valid phone number(it must be 10 characters)'})
                                   
    house_rent=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control border border-dark','placeholder':'House Rent In Rupees (per month)'}),label='')


    
    
class PublishHouseOnSaleForm(forms.ModelForm):
    class Meta:
        model=HouseOnSell
        fields=['house_photos','house_type','about_house','house_location','city_name','Owner_name','contact_number','house_price']
        labels={'house_photos':'Add Photo'}


    about_house=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control border border-dark mt-2','placeholder':'Write Something About this house...',"rows":"7"}),label='')

    house_location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'Location of house'}),label='')

    city_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'City'}),label='')

    Owner_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'Name Of Owner'}),label='')

    contact_number=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control border border-dark','placeholder':'Contcat number of owner'}),label='',error_messages={'max_length':'Please Enter the valid phone number(it must be 10 characters)'})
                                   
    house_price=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control border border-dark','placeholder':'House Price In Rupees '}),label='')



#-----SECURITY------
class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
        labels={
            'username':'',
            'email':''
        }

        widgets={

            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username(must be unique)'}),

            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),

            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),

            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}),label='')

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype Password'}),label='')


class LoginUserForm(AuthenticationForm):


    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','autofocus': True}),label='')

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter The Password','autofocus': True}),label='')