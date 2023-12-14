from rest_framework import serializers

from food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price')
        model = Food
