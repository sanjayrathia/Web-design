from django.db import models

# Create your models here.
class Contact(models.Model):
    fname  = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    areacode =  models.CharField(max_length=122)
    telnum = models.CharField(max_length=122 ,default='10000')
    email = models.CharField(max_length=122)
    approve= models.BooleanField(default=False)
    feedback = models.TextField()
    def __str__(self):
        return self.fname