from django.contrib import admin
from .models import AdImage

# Register your models here.
@admin.register(AdImage)
class AdImage(admin.ModelAdmin):
    list_display = ('id',)
