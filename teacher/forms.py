from django import forms
from teacher.models import Teacher
class TeacherForm(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = "__all__"
