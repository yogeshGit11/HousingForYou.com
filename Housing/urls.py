from HousingApp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='homepage'),
    path('AdminUserActivities/',views.AdminUserActivities,name='AdminUserActivity'),
    path('HouseOnRent/',views.ViewHousesOnRent.as_view(),name='HouseOnRent'),
    path('HouseOnSale/',views.ViewHousesOnSale.as_view(),name='HouseOnSale'),
    path('UserChoiceRentHouse/',views.GetUserChoiceRentRooms,name='userchoiceRentRooms'),
    path('UserChoiceSaleHouse/',views.GetUserChoiceSaleRooms,name='userchoiceSaleRooms'),
    path('UserChoiceCityRentHouse/',views.GetUserChoiceCityRentRooms,name='userchoiceCityRentRooms'),
     path('UserChoiceCitySaleHouse/',views.GetUserChoiceCitySaleRooms,name='userchoiceCitySaleRooms'),
    path('PublishHouseOnRent/',views.PublishHouseOnRent.as_view(),name='PublishHouseOnRent'),
    path('PublishHouseOnSale/',views.PublishHouseOnSale.as_view(),name='PublishHouseOnSale'),
    path('MyActivities/',views.OwnerActivities,name='OwnerActivities'),
    path('UpdateRentHouseInfo/<int:pk>',views.UpdateRentHouse.as_view(),name='UpdateRentHouse'),
    path('UpdateSaleHouseInfo/<int:pk>',views.UpdateSaleHouse.as_view(),name='UpdateSaleHouse'),

    path('RemoveRentHouseInfo/<int:id>',views.RemoveRentHouse,name='RemoveRentHouse'),
    path('RemoveSaleHouseInfo/<int:id>',views.RemoveSaleHouse,name='RemoveSaleHouse'),

    path('RegisterUser/',views.RegisterUser.as_view(),name='RegisterUser'),
    path('LoginUser/',views.LoginUser.as_view(),name='LoginUser'),
    path('LogoutUser/',views.LogoutUser.as_view(),name='LogoutUser'),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)