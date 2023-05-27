from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import ListView,TemplateView,CreateView,UpdateView,DeleteView
from .models import HouseOnRent,HouseOnSell
from .forms import PublishHouseOnRentForm,PublishHouseOnSaleForm,RegisterUserForm,LoginUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.models import User

class HomePage(TemplateView):
    template_name='home.html'

class ViewHousesOnRent(ListView):
    model=HouseOnRent
    template_name='ViewHousesOnRent.html'
    context_object_name='houses'
    paginate_by=10

class ViewHousesOnSale(ListView):
    model=HouseOnSell
    template_name='ViewHousesOnSale.html'
    context_object_name='houses'
    paginate_by=10

def GetUserChoiceRentRooms(request):
    if request.method == 'POST':
        roomtype=request.POST['userchoice']
        if roomtype == 'View All':
            return redirect('/HouseOnRent/')
        else:
            usertyperoom=HouseOnRent.objects.filter(house_type__roomtype=roomtype)
            return render(request,'ViewHousesOnRent.html',{'houses':usertyperoom})

def GetUserChoiceSaleRooms(request):
    if request.method == 'POST':
        roomtype=request.POST['userchoice']
        if roomtype == 'View All':
            return redirect('/HouseOnSale')
        else:
            usertyperoom=HouseOnSell.objects.filter(house_type__roomtype=roomtype)
            return render(request,'ViewHousesOnSale.html',{'houses':usertyperoom})
        
def GetUserChoiceCityRentRooms(request):
     if request.method=='POST':
          city=request.POST['cityname']

          roomcity=set(HouseOnRent.objects.filter(city_name=city))
          return render(request,'ViewHousesOnRent.html',{'houses':roomcity})

def GetUserChoiceCitySaleRooms(request):
     if request.method=='POST':
          city=request.POST['cityname']

          roomcity=set(HouseOnSell.objects.filter(city_name=city))
          return render(request,'ViewHousesOnSale.html',{'houses':roomcity})        

class PublishHouseOnRent(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model=HouseOnRent
    form_class=PublishHouseOnRentForm
    template_name='owner/PublishHouseOnRent.html'
    context_object_name='form'
    success_url='/PublishHouseOnRent/'
    success_message='House Published For Rent.'
    login_url='/LoginUser/'

class PublishHouseOnSale(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model=HouseOnSell
    form_class=PublishHouseOnSaleForm
    template_name='owner/PublishHouseOnSale.html'
    context_object_name='form'
    success_url='/PublishHouseOnSale/'
    success_message='House Published For Sale.'
    login_url='/LoginUser/'

        
def OwnerActivities(request):
        rent=HouseOnRent.objects.filter(user_name=request.user) 
        sell=HouseOnSell.objects.filter(user_name=request.user) 
        
        return render(request,'owner/OwnerActivities.html',{'rentdata':rent,'selldata':sell})

def AdminUserActivities(request):
        rent=HouseOnRent.objects.exclude(user_name__username='AdminUser')
        sell=HouseOnSell.objects.exclude(user_name__username='AdminUser')
        
        return render(request,'owner/OwnerActivities.html',{'rentdata':rent,'selldata':sell})

class UpdateRentHouse(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = HouseOnRent
    form_class=PublishHouseOnRentForm
    template_name='owner/UpdateRentHouseData.html'
    context_object_name='form'
    success_message='Updated Successfully!!!'

    def get_success_url(self):
           return reverse("OwnerActivities")
    
class UpdateSaleHouse(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = HouseOnSell
    form_class=PublishHouseOnSaleForm
    template_name='owner/UpdateSaleHouseData.html'
    context_object_name='form'
    success_message='Updated Successfully!!!'

    def get_success_url(self):
           return reverse("OwnerActivities")
    

def RemoveRentHouse(request,id):
    if request.method=='POST':
        house=HouseOnRent.objects.get(pk=id)
        house.delete()
        return HttpResponseRedirect('/MyActivities')


def RemoveSaleHouse(request,id):
    if request.method=='POST':
        house=HouseOnSell.objects.get(pk=id)
        house.delete()
        return HttpResponseRedirect('/MyActivities')
    
class ViewOwnerDetails(ListView):
     model=User
     context_object_name='users'
     template_name='OwnerDetails.html'

def VisitOwnerData(request,owner):
     RentHouses=HouseOnRent.objects.filter(user_name__username=owner)
     SellHouses=HouseOnSell.objects.filter(user_name__username=owner)

     return render(request,'VisitOwnerData.html',{'renthouse':RentHouses,'salehouse':SellHouses,'username':owner})

def DeleteOwner(request,id):
    if request.method=='POST':
        user=User.objects.get(pk=id)
        user.delete()
        return HttpResponseRedirect('/ViewOwnerDetails')

#-----SECURITY------

class RegisterUser(SuccessMessageMixin,CreateView):
    form_class=RegisterUserForm
    template_name='auth/RegisterUser.html'
    success_url='/RegisterUser/'
    success_message='Registration Successfully!!! Now you can login.'


class LoginUser(SuccessMessageMixin,LoginView):
    authentication_form=LoginUserForm
    template_name='auth/LoginUser.html'
    success_url='/LoginUser/'


class LogoutUser(SuccessMessageMixin,LogoutView):
    template_name='auth/LoginUser.html'
