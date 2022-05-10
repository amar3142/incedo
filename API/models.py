from django.db import models

# Create your models here.

class Search_object(models.Model):
    search_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.search_name