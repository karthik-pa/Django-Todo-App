from django.db import models

class todos(models.Model):
    title=models.CharField(max_length=200)


