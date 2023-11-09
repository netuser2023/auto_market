from django.db import models

# Create your models here.

class Auto(models.Model):
    auto = models.CharField(max_length=30, null=True)
    auto_features = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.auto