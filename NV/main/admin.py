from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Profession)
admin.site.register(People)
admin.site.register(VisRate)

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('profession',)  # Здесь указываем, какие поля модели отображать в списке объектов



