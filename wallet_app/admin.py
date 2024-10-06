from django.contrib import admin

# Register your models here.
from .models import Account, Transfer

admin.site.register(Account)
admin.site.register(Transfer)