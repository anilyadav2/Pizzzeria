
from django.db import models
class Pizza(models.Model):
    """A topic the user is learning about."""
    Pizaa_name = models.CharField(max_length=400)
    date_added = models.DateTimeField(
            auto_now_add=True)
    def __str__(self):
        return self.text