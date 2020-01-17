from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10, unique=True)
    name= models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.mobile_no

class HospitalAccess(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.status

class AccessRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    reason = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.id
