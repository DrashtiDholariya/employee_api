from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee

class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        self.employee_data = {
            'name': 'ashish kumar',
            'email': 'ashish@gmail.com',
            'department': 'Engineering',
            'role': 'Developer'
        }

    def test_create_employee(self):
        response = self.client.post('/api/employees/', self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

    def test_create_employee_duplicate_email(self):
        self.client.post('/api/employees/', self.employee_data)
        response = self.client.post('/api/employees/', self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        Employee.objects.create(**self.employee_data)
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.get(f'/api/employees/{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.delete(f'/api/employees/{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)