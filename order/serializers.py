from rest_framework import serializers

from order.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'order_status', 'total')
        model = Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'food', 'order', 'quantity')
        model = OrderItem


class OrderWithItemsSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer

    class Meta:
        fields = ('id', 'order_status', 'total', 'order_items')
        model = Order
