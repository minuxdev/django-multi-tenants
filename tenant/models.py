from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True


class Domain(DomainMixin):
    pass