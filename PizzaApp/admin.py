from django.contrib import admin

# Register your models here.

from .models import Entry, Topic,Topin

admin.site.register(Topic)
admin.site.register(Topin)
admin.site.register(Entry)
