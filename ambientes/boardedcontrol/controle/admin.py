from django.contrib import admin
from .models import Rede, Sensor, Atuador, Mqtt, Embarcado

# Register your models here.
admin.site.register(Rede)
admin.site.register(Sensor)
admin.site.register(Atuador)
admin.site.register(Mqtt)
admin.site.register(Embarcado)
