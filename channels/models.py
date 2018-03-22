from django.db import models

# Create your models here   .

class Channel(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    subscriberCount = models.IntegerField()

    def __str__(self):
        return "name : " + self.name + ", country : " + self.country + ", subscribers : " + str(self.subscriberCount)
