from django.db import models

class Allotment(models.Model):
    tag_id = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    action = models.CharField(max_length=50)