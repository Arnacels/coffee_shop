import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashid_field import HashidAutoField
from discount.models import BoughtCoffee


class DiscountCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    barcode = models.CharField(null=True, max_length=18)
    bonus_card = models.DecimalField(null=True, max_digits=40, decimal_places=2, default=0)
    active = models.BooleanField()
    date_last_update = models.DateField(auto_now_add=True, db_index=True)
    date_create = models.DateField(auto_now_add=True, db_index=True)

    def generator_barcode(self):
        self.barcode = str(random.randrange(10101010101, 100000000000))
        self.save()


class Users(AbstractUser):
    id = HashidAutoField(primary_key=True)
    card = models.ForeignKey(DiscountCard, on_delete=models.CASCADE, related_name="referal", null=True, blank=True)

    def check_my_bonus(self):
        query = BoughtCoffee.objects.filter(user_id=self.id)
        c = 0
        for item in query:
            c+=item.cost
        if c > self.card.bonus_card:
            self.card.bonus_card = c
            self.card.save()