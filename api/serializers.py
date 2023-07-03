from rest_framework import serializers
from .models import Order

class ImportOrderSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format="%d/%b/%Y")
   
    class Meta:
        model = Order
        fields = '__all__'
        #fields = ['order_number', 'total_price', 'created_time', 'payment_status', 'shipping_address']
