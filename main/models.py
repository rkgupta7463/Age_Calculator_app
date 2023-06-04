from django.db import models

# Create your models here.

class Age_Table(models.Model):
    full_name=models.CharField(max_length=80)
    gender=models.CharField(max_length=10)
    birth_year=models.CharField(max_length=10)
    birth_month=models.CharField(max_length=10)
    birth_day=models.CharField(max_length=10)

    def __str__(self):
        return self.full_name