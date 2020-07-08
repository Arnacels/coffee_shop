from django.db import models
from hashid_field import HashidAutoField


class Coffee(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=18, null=True, blank=True)
    cost = models.DecimalField(null=True, blank=True, max_digits=40, decimal_places=2)


class BoughtCoffee(models.Model):
    id = HashidAutoField(primary_key=True)
    user_id = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(auto_now_add=True, db_index=True)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name="coffee")
    cost = models.DecimalField(null=True, blank=True, max_digits=40, decimal_places=2)
    with_card = models.BooleanField(default=True)
