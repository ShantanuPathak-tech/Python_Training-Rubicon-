from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
import csv
from django.http import HttpResponse

def home(request):
    return render(request, "students/home.html")

def student_list(request):
    students = Student.objects.all().order_by("-marks")
    return render(request, "students/student_list.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        marks = request.POST["marks"]
        department = request.POST["department"]
        Student.objects.create(name=name, marks=marks, department=department)
        return redirect("student_list")
    return render(request, "students/add_student.html")

def search_student(request):
    query = request.GET.get("q", "")
    students = Student.objects.filter(name__icontains=query)
    return render(request, "students/search.html", {"students": students, "query": query})

def high_scorers(request):
    students = Student.objects.filter(marks__gte=80).order_by("-marks")
    return render(request, "students/high_scorers.html", {"students": students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST["name"]
        student.marks = request.POST["marks"]
        student.department = request.POST["department"]
        student.save()
        return redirect("student_list")
    return render(request, "students/edit_student.html", {"student": student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    
def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Marks', 'Department', 'Grade'])

    students = Student.objects.all().order_by('-marks')
    for student in students:
        writer.writerow([student.id, student.name, student.marks, student.department, student.get_grade()])

    return response


def student_stats(request):
    total_students = Student.objects.count()
    if total_students > 0:
        avg_marks = sum(s.marks for s in Student.objects.all()) / total_students
    else:
        avg_marks = 0

    departments = Student.objects.values_list('department', flat=True).distinct()
    
    return render(request, "students/stats.html", {
        "total_students": total_students,
        "avg_marks": round(avg_marks, 2),
        "departments": list(departments)
    })