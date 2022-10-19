from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from .models import Teacher
from django.contrib import messages

# Create your views here.
def index(request):
  students = Student.objects.all()
  return render(request, "student/index.html", {'students': students})

def new(request):
  teachers = Teacher.objects.all()
  return render(request, "student/new.html", {'teachers': teachers})

def show(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)
  return render(request, "student/show.html", {'student': student})

def edit(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)
  return render(request, "student/edit.html", {'student': student})

def destroy(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)
  student.delete()
  messages.success(request, 'Contact Deleted Successfully!')
  return redirect("index")

def find_student(request, id):
  student = Student.objects.get(id=id)
  return student

def create(request):
  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('show')
      except:
        pass
  else:
    form = StudentForm()
  return render(request, 'student/index.html', {'form': form})

def update(request, id):
  student = find_student(request, id)
  # student = Student.objects.get(id=id)

  form = StudentForm(request.POST, instance = student)
  print("+++++++++++++++++++++++")
  print(student)
  print(form.is_valid())
  print(form)
  print("+++++++++++++++++++++++")
  if form.is_valid():
    form.save()
    return redirect("show")
  return render(request, 'student/edit.html', {'student': student})
