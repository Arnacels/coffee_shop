import datetime
from rest_framework import serializers
from .models import Coffee, BoughtCoffee
from hashid_field.rest import HashidSerializerCharField
from account.models import Users, DiscountCard
from django.http import HttpResponse


class BoughtCoffeeSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field='discount.Coffee.id'), read_only=True)
    coffee = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='discount.Coffee.id'), queryset=Coffee.objects.all())
    name_bayer = serializers.SerializerMethodField()

    def get_name_bayer(self, obj):
        return Users.objects.get(id=obj.user_id).first_name

    class Meta:
        model = BoughtCoffee
        fields = ('id', 'name_bayer' ,'user_id', 'date', 'coffee', 'cost', 'with_card')


class CoffeeSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field='discount.BoughtCoffee.id'), read_only=True)

    class Meta:
        model = Coffee
        fields = ('id', 'name', 'cost')


class CreateBoughtCoffeeSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field='discount.BoughtCoffee.id'), read_only=True)
    coffee = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='discount.Coffee.id'), queryset=Coffee.objects.all())

    def create(self, validated_data):
        if validated_data.get('user_id') and validated_data.get('user_id') != '':
            user = Users.objects.get(id=validated_data.get('user_id'))
            coffee = validated_data.get('coffee')
            if user and coffee:
                cost = coffee.cost
                card_user = user.card
                if datetime.timedelta(validated_data.get('date') - card_user.date_last_update).days / 182 < 6:
                    if card_user.active:
                        if validated_data.get('with_card'):
                            card_user.bonus_card += cost
                            card_user.save()
                return BoughtCoffee(user_id=validated_data.get('user_id'),
                                    coffee=validated_data.get('coffee'),
                                    cost=cost)

    class Meta:
        model = BoughtCoffee
        fields = ('id', 'user_id', 'date', 'coffee', 'cost', 'with_card')
