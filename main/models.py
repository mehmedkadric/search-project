from django.db import models

class Search(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=255)

    def __str__(self):
        return self.query
    

class Data(models.Model):
    city = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.state_name}"