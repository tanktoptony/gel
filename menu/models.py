from django.db import models

# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.name
