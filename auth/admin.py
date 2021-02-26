from django.contrib import admin

from .models import Signup
from .models import Message

admin.site.register(Signup)
admin.site.register(Message)
# Register your models here.
