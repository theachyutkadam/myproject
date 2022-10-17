from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('index', views.index, name="index-page"),
  path('new', views.new),
  path('create', views.create),

  path('show/<int:id>', views.show),
  path('edit/<int:id>', views.edit),

  path('update/<int:id>', views.update),
  path('delete/<int:id>', views.destroy),
]

