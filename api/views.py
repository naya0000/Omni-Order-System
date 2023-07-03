# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseBadRequest
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Order, OrderStatus

# ACCEPTED_TOKEN = 'omni_pretest_token'

# def validate_access_token(view_func):
#     def wrapper(request, *args, **kwargs):
#         access_token = request.data.get('access_token')
#         if access_token != ACCEPTED_TOKEN:
#             return HttpResponseBadRequest('Invalid access token')
#         return view_func(request, *args, **kwargs)
#     return wrapper


# @api_view(['POST'])
# @validate_access_token
# def import_order(request):
#     order_number = request.data.get('order_number')
#     total_price = request.data.get('total_price')
#     created_time = request.data.get('created_time')
#     payment_status = request.data.get('payment_status', 'pending')
#     shipping_address = request.data.get('shipping_address', '')

#     order = Order(
#         order_number=order_number,
#         total_price=total_price,
#         created_time=created_time,
#         payment_status=payment_status,
#         shipping_address=shipping_address
#     )
#     order.save()

#     # Create an initial order status entry
#     initial_status = OrderStatus(order=order, status='Pending')
#     initial_status.save()

#     print(order)
#     return Response('Order imported successfully', status=200)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImportOrderSerializer
from .models import Order, OrderStatus

ACCEPTED_TOKEN = 'omni_pretest_token'

def validate_access_token(view_func):
    def wrapper(request, *args, **kwargs):
        access_token = request.data.get('access_token')
        if access_token != ACCEPTED_TOKEN:
            return Response('Invalid access token', status=400)
        return view_func(request, *args, **kwargs)
    return wrapper


@api_view(['POST'])
@validate_access_token
def import_order(request):
    serializer = ImportOrderSerializer(data=request.data)
    
    if serializer.is_valid():
        validated_data = serializer.validated_data

        #print(validated_data)
        order = Order.objects.create(
            order_number=validated_data['order_number'],
            total_price=validated_data['total_price'],
            created_time=validated_data['created_time'],
            payment_status=validated_data.get('payment_status', 'pending'),
            shipping_address=validated_data.get('shipping_address', ''),
        )
        order.save()

        initial_status = OrderStatus(order=order, status='Pending')
        initial_status.save()

        #print(order)
        return Response('Order imported successfully', status=200)

    return Response(serializer.errors, status=400)

