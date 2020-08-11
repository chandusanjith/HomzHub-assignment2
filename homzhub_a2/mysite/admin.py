from django.contrib import admin
from .models import StateMaster,RequestTypeMaster, StatusMaster, UserRequest


admin.site.register(StateMaster)
admin.site.register(RequestTypeMaster)
admin.site.register(StatusMaster)
admin.site.register(UserRequest)