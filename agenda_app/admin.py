from django.contrib import admin
from agenda_app.models import agendaItems,agendalist

# Register your models here.
admin .site .register(agendalist)
admin .site .register(agendaItems)
