from django.contrib import admin
from .models import Coffee, BoughtCoffee

@admin.register(Coffee)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost']
    fieldsets = (
        ('General info', {
         'fields': ('name', 'cost')
         }),
    )


@admin.register(BoughtCoffee)
class DiscountCard(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'date', 'coffee', 'cost']
    fieldsets = (
        ('General info', {
         'fields': ('user_id', 'date', 'coffee', 'cost')
         }),
    )
    search_fields = ['date']

