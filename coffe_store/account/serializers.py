from rest_framework import serializers
from .models import DiscountCard, Users
from rest_framework.validators import UniqueValidator
from hashid_field.rest import HashidSerializerCharField
from discount.models import Coffee


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=Users.objects.all())])
    username = serializers.CharField(max_length=32,
                                     validators=[UniqueValidator(queryset=Users.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        card = DiscountCard(bonus_card=0, active=False)
        card.generator_barcode()
        card.save()
        user = Users.objects.create_user(validated_data['username'], validated_data['email'],
                                         validated_data['password'], card=card)
        return user

    class Meta:
        model = Users
        fields = ('username', 'email', 'password',)


class AllUsersSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field='account.Users.id'), read_only=True)
    my_money = serializers.SerializerMethodField()
    drinks = serializers.SerializerMethodField()

    def get_my_money(self, obj):
        return obj.card.bonus_card if obj.username != 'admin' else None

    def get_drinks(self, obj):
        if obj.username != 'admin':
            money = obj.card.bonus_card
            info = []
            for item in Coffee.objects.all():
                total = money // item.cost
                info.append((total, item.name))
            return info
        return None

    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'card', 'my_money', 'drinks')


class CreateCardSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        card = DiscountCard(active=validated_data['active'])
        card.generator_barcode()
        return card

    class Meta:
        model = DiscountCard
        fields = ('id', 'bonus_card', 'active', 'date_last_update', 'date_create', 'barcode')
        # fields = ['active']
