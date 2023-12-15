from django.urls import path
from rest_framework.routers import SimpleRouter

from order.views import OrderViewSet


router = SimpleRouter()
router.register('', OrderViewSet, basename='orders')
# router.register('', OrderItemViewSet, basename='order_items')

urlpatterns = router.urls
