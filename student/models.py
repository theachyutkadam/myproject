from django.db import models
from teacher.models import Teacher

# Create your models here.
class Student(models.Model):
  contact = models.CharField(max_length=10)
  address = models.TextField()
  birth_date = models.DateField(auto_now=False)
  is_active = models.BooleanField(default=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

  class Meta:
    db_table = "student"
