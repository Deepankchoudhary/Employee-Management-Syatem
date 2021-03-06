from django.db import models

from django.contrib.auth.models import User


class EmployeeDetail(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
