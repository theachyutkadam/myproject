from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
  list_display = ('id', 'contact', 'address', 'is_active', 'birth_date')

# Register your models here.
admin.site.register(Student, StudentAdmin)
