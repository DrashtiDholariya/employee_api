from django.db import models
from django.core.validators import EmailValidator

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address.")])
    department = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., HR, Engineering, Sales")
    role = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., Manager, Developer, Analyst")
    date_joined = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['department']),
            models.Index(fields=['role']),
        ]

    def __str__(self):
        return f"{self.name} - {self.email}"