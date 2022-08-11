from django.db import models

# Create your models here.
class AdImage(models.Model):
    image = models.ImageField(upload_to ='upload/images',null=False,blank=False)
