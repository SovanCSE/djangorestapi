from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeProfile(models.Model):
    level_choice = [('Manager', 'level1'),
    ('Senor Developer', 'level2'),
    ('Junior Developer', 'level3'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=level_choice)
    salary = models.DecimalField(max_digits=30, decimal_places=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

