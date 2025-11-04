from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Product, Orders, Feedback
from django.core.files.uploadedfile import SimpleUploadedFile

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            first_name='Test',
            last_name='User'
        )
        self.customer = Customer.objects.create(
            user=self.user,
            address='123 Test St',
            mobile='1234567890'
        )

    def test_customer_creation(self):
        self.assertTrue(isinstance(self.customer, Customer))
        self.assertEqual(self.customer.__str__(), 'Test')

    def test_get_name(self):
        self.assertEqual(self.customer.get_name, 'Test User')

    def test_get_id(self):
        self.assertEqual(self.customer.get_id, self.user.id)

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=100,
            description='Test Description'
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), 'Test Product')

class OrdersModelTest(TestCase):
    def setUp(self):
        # Create a user and customer first
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.customer = Customer.objects.create(
            user=self.user,
            address='123 Test St',
            mobile='1234567890'
        )
        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            price=100,
            description='Test Description'
        )
        # Create an order
        self.order = Orders.objects.create(
            customer=self.customer,
            product=self.product,
            email='test@example.com',
            address='123 Test St',
            mobile='1234567890',
            status='Pending'
        )

    def test_order_creation(self):
        self.assertTrue(isinstance(self.order, Orders))
        self.assertEqual(self.order.status, 'Pending')
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.product, self.product)

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            name='Test User',
            feedback='This is a test feedback'
        )

    def test_feedback_creation(self):
        self.assertTrue(isinstance(self.feedback, Feedback))
        self.assertEqual(self.feedback.__str__(), 'Test User')
        self.assertTrue(self.feedback.date is not None)
