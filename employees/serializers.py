from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'role', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def validate_name(self, value):
        if not value or value.strip() == '':
            raise serializers.ValidationError("Name cannot be empty.")
        return value.strip()

    def validate_email(self, value):
        if not value or value.strip() == '':
            raise serializers.ValidationError("Email cannot be empty.")
        return value.lower().strip()

    def validate(self, data):
        # Check for duplicate email on create
        if self.instance is None:  # Create operation
            if Employee.objects.filter(email=data.get('email')).exists():
                raise serializers.ValidationError({
                    "email": "Employee with this email already exists."
                })
        else:  # Update operation
            if Employee.objects.filter(email=data.get('email')).exclude(
                id=self.instance.id
            ).exists():
                raise serializers.ValidationError({
                    "email": "Employee with this email already exists."
                })
        return data