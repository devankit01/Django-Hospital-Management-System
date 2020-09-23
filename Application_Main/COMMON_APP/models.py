from django.db import models
from django.contrib.auth.models import User
from DOCTER.models import *
from PATIENT.models import *
# Create your models here.

# Model For Receptionist
class Receptionist(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	address = models.CharField(max_length=200)
	username = models.OneToOneField(User,on_delete = models.CASCADE)



# Model For Appointment
class Appointment(models.Model):
	docterid = models.ForeignKey('DOCTER.Docter',on_delete = models.CASCADE)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	time = models.CharField(max_length =40)
	date = models.CharField(max_length=40,default="")
	status = models.BooleanField(max_length = 15, default=0)


# Model For HR
class HR(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	address = models.CharField(max_length=200)
	username = models.OneToOneField(User,on_delete = models.CASCADE)