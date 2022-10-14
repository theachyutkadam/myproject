from email.policy import default
from django.db import models

# Create your models here.
class Student(models.Model):
  # id = models.CharField(max_length=20)
  # ename = models.CharField(max_length=100)
  # eemail = models.EmailField()
  contact = models.CharField(max_length=10)
  address = models.TextField()
  birth_date = models.DateField(auto_now=False)
  is_active = models.BooleanField(default=True)

  class Meta:
    db_table = "student"
