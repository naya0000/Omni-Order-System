from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order, OrderStatus, Product, OrderItem

class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_import_order(self):
        url = '/api/import_order/'
        data = {
            'access_token': 'omni_pretest_token',
            'order_number': '12345',
            'total_price': '200.00',
            'created_time': '2022-01-01T00:00:00Z',
            'payment_status': '123',
            'shipping_address': '123 Street, City'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderStatus.objects.count(), 1)

        order = Order.objects.first()
        order_status = OrderStatus.objects.first()
        self.assertEqual(order.order_number, '12345')
        self.assertEqual(order_status.status, 'Pending')
       
        #Invalid access token
        data = {
            'access_token': 'invalid_token',
            'order_number': '54321',
            'total_price': '200.00',
            'created_time': '2022-02-02T00:00:00Z',
            'payment_status': 'pending',
            'shipping_address': '123 Street, City'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 1)

class OrderItemTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.order = Order.objects.create(order_number='12345', total_price=100.00)
        self.product = Product.objects.create(name='Product 1', price=10.00)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2)
        self.order_status = OrderStatus.objects.create(order=self.order,status='paid')

    def test_order_item_creation(self):
        # Test if the order item is created correctly
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.quantity, 2)

    def test_order_item_str(self):
        # Test the __str__ method of the order item
        expected_str = f"{self.order} - {self.product}"
        self.assertEqual(str(self.order_item), expected_str)
    
class OrderStatusTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.order = Order.objects.create(order_number='12345', total_price=100.00)
        self.order_status = OrderStatus.objects.create(order=self.order, status='paid')

    def test_order_status_creation(self):
        # Test if the order status is created correctly
        self.assertEqual(self.order_status.order, self.order)
        self.assertEqual(self.order_status.status, 'paid')