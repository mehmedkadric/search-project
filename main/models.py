from django.db import models

# Create your models here.

class Search(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=255)

    def __str__(self):
        return self.query