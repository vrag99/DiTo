from django.contrib import admin
from .models import Diary, ToDo

# Register your models here.
admin.site.register(Diary)
admin.site.register(ToDo)