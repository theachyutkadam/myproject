from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

# Create your views here.
def index(request):
  teachers = Teacher.objects.all()
  return render(request, "teacher/index.html", {'teachers': teachers})

def new(request):
  return render(request, "teacher/new.html")

def show(request, id):
  teacher = find_teacher(request, id)
  # teacher = Teacher.objects.get(id=id)
  return render(request, "teacher/show.html", {'teacher': teacher})

def edit(request, id):
  teacher = find_teacher(request, id)
  # teacher = Teacher.objects.get(id=id)
  return render(request, "teacher/edit.html", {'teacher': teacher})

def destroy(request, id):
  teacher = find_teacher(request, id)
  # teacher = Teacher.objects.get(id=id)
  teacher.delete()
  return redirect("teacher/index/")

def find_teacher(request, id):
  teacher = Teacher.objects.get(id=id)
  return teacher

def create(request):
  if request.method == "POST":
    form = TeacherForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('show')
      except:
        pass
  else:
    form = TeacherForm()
  return render(request, 'teacher/index.html', {'form': form})

def update(request, id):
  teacher = find_teacher(request, id)
  # teacher = Teacher.objects.get(id=id)

  form = TeacherForm(request.POST, instance = teacher)
  print("+++++++++++++++++++++++")
  print(teacher)
  print(form.is_valid())
  print(form)
  print("+++++++++++++++++++++++")
  if form.is_valid():
    form.save()
    return redirect("show")
  return render(request, 'teacher/edit.html', {'teacher': teacher})
