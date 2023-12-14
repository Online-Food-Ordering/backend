from django.urls import path

from food.views import FoodList, FoodDetail

urlpatterns = [
    path('<int:pk>/', FoodDetail.as_view()),
    path('', FoodList.as_view())
]