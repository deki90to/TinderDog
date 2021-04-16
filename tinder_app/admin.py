from django.contrib import admin
from . models import *


admin.site.register(DogBreed)
# admin.site.register(Dog)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
	list_display = ('user', 'breed', 'gender', 'birthYear', 'phone_no', 'date')
	list_filter = ('date', 'breed', 'gender', 'birthYear', 'user')
	ordering = ('-date',)
	search_fields = ('gender', 'birthYear', 'info', 'phone_no', 'date')