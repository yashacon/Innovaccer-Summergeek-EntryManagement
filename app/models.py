from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Entries(models.Model):
    host_name=models.CharField(max_length=100)
    host_email=models.EmailField()
    host_phone=PhoneNumberField()  
    visitor_name=models.CharField(max_length=100)
    visitor_email=models.EmailField()
    visitor_phone=PhoneNumberField()
    checkin=models.DateTimeField(default=datetime.now,blank=True)
    checkout=models.DateTimeField(null=True,blank=True)
    inside=models.BooleanField(default=True,blank=True)
    def __str__(self):
        return 'Test number {} is {}'.format(self.pk, self.inside)