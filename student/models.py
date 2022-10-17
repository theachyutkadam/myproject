from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
  contact = models.CharField(max_length=10)
  address = models.TextField()
  birth_date = models.DateField(auto_now=False)
  is_active = models.BooleanField(default=True)
  # teacher_id = models.ManyToManyField('teacher')

  class Meta:
    db_table = "student"
