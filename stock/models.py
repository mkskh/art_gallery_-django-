from django.db import models

# Create your models here.
class Warehouse(models.Model):
    location = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)


class Visitor(models.Model):
    visitor_name = models.CharField(max_length=150)
    ome_of_visit = models.DateTimeField(auto_now=True)
    purchases = models.TextField()

    def __str__(self):
        return f"{self.visitor_name}, {self.ome_of_visit}, {self.purchases}"

