from django.db import models

# Create your models here.
#AGREGAMOS LOS MODELOS QUE TENEMOS EN MONGODB

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)