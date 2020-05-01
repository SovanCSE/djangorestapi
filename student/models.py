from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    level_choice = [('Senior', 'level1'),
    ('Sub Senior', 'level2'),
    ('Junior', 'level3'),
    ]
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered "
                                                                   "in the format: '+999999999'. Up to 15 digits allowed.")
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    class_level = models.CharField(max_length=20, choices=level_choice)
    total_marks = models.FloatField()
    roll_no = models.IntegerField(unique=True)
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('first_name', 'last_name',)
        ordering = ['-updated_date']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'