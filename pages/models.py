from django.db import models

class Video(models.Model):
    url = models.CharField(max_length=200, default="")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

class Page(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    subscript = models.CharField(max_length=200, default="")
    startTime = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)