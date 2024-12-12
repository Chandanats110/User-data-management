from django.db import models

class userdata(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)


class status(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    upload_time = models.TimeField()
    user = models.ForeignKey(userdata,related_name='user',on_delete=models.CASCADE) 
