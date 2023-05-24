from django.contrib import admin
from .models import HouseOnRent,HouseOnSell,HouseType

admin.site.register(HouseType)
admin.site.register(HouseOnRent)
admin.site.register(HouseOnSell)
