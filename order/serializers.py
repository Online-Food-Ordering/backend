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
