from django.shortcuts import render
from rest_framework import generics

from food.models import Food
from food.serializers import FoodSerializer


# Create your views here.


class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
