from django.db import models

# Create your models here.
from django.db import models
class Pizza_name(models.Model):
    
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(
            auto_now_add=True)
    def __str__(self):
        return self.text