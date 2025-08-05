from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    username = models.CharField(max_length=50,null=False,blank=False)
    email = models.CharField(max_length=50,null=False,blank=False)
    zipCode = models.CharField(max_length=50,null=False,blank=False)
    # photo = models.ImageField(upload_to='usersPhoto/',blank=True,null=True)
    dateCreatedAt = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)



    def __str__(self):
        return self.first_name + " " + self.last_name

