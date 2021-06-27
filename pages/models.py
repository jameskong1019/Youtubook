from django.db import models


class Page(models.Model):
    subscript = models.CharField(max_length=200)
    startTime = models.DecimalField(max_digits=30, decimal_places=2)
