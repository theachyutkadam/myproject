from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
  list_display = ('id', 'contact', 'address', 'is_active', 'birth_date')

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
