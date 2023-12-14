from rest_framework.routers import SimpleRouter

from food.views import FoodViewSet

router = SimpleRouter()
router.register('', FoodViewSet, basename='foods')

urlpatterns = router.urls
