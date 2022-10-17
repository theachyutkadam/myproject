from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('index', views.index, name="index-page"),
  path('new', views.new , name="new-page"),
  path('create', views.create , name="create-page"),

  path('show/<int:id>', views.show , name="show-page"),
  path('edit/<int:id>', views.edit , name="edit-page"),

  path('update/<int:id>', views.update , name="update-page"),
  path('delete/<int:id>', views.destroy , name="destroy-page"),
]

