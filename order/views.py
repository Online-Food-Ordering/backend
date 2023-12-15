from rest_framework import viewsets
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderWithItemsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderWithItemsSerializer

    def list(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer = OrderWithItemsSerializer(queryset, many=True)
        return Response(serializer.data)
