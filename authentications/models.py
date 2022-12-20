from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=16)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} | {self.email} | {self.created_on}"
    