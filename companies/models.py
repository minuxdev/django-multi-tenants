from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)


    def __str__(self):
        return f"{self.name} | {self.email} | {self.created_on}"
