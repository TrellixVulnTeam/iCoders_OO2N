from django.db import models


# Create your models here.

class Contact(models.Model):
    snos=models.AutoField(primary_key=True)
    name=models.CharField( max_length=255)
    email=models.EmailField(max_length=254)
    phone=models.CharField( max_length=50)
    description=models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    



    def __str__(self):
        return 'message from' + ' ' + self.name + ' ' + self.email
    

