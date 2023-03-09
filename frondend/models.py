from django.db import models


class f_login(models.Model):
    username=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Confirmpassword=models.CharField(max_length=30,null=True,blank=True)

class checkoutdb(models.Model):
    FIRSTNAME=models.CharField(max_length=30,null=True,blank=True)
    ADRESS=models.CharField(max_length=30,null=True,blank=True)
    TOTAL=models.IntegerField(null=True,blank=True)
    PINCODE=models.IntegerField(null=True,blank=True)
    CARDNUMBER=models.IntegerField( null=True, blank=True)