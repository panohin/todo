from django.contrib import admin

from .models import Target, FilterName, Emails

admin.site.register(Target)
admin.site.register(FilterName)
admin.site.register(Emails)
