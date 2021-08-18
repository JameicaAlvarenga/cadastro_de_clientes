from django.contrib import admin
from .models import Custumer

@admin.register(Custumer)
class CustumerAdmin(admin.ModelAdmin):
    list_display = ["id", "frist_name", "last_name", "email"]
