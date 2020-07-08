from django.contrib import admin
from .models import Users, DiscountCard


@admin.register(Users)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'email', 'card']
    fieldsets = (
        ('General info', {
         'fields': ('first_name', 'last_name', 'email', 'card')
         }),
    )
    search_fields = ('email', 'last_name', 'first_name')


@admin.register(DiscountCard)
class DiscountCard(admin.ModelAdmin):
    list_display = ['id', 'bonus_card', 'active', 'date_last_update', 'date_create']
    fieldsets = (
        ('General info', {
         'fields': ('bonus_card', 'active', 'date_last_update', 'date_create')
         }),
    )
    search_fields = ['date_last_update']

