from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    admission = models.IntegerField()
    course = models.CharField(max_length=20)

    class Meta:
        db_table = "student"
