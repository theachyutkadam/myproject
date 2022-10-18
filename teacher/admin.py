from django.contrib import admin

class TeacherAdmin(admin.ModelAdmin):
  list_display = ('id', 'contact', 'address', 'is_active', 'birth_date')

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
