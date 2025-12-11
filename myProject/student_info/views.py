from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from student_info.models import Student
# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            image = request.POST.get('image')
        )
        
        return redirect('all_student')
    return render (request, 'student/add_student.html')

def all_student(request):
    query = request.GET.get('query')
    studentData = Student.objects.all()
    if query:
        studentData = Student.objects.filter(
            Q(name__icontains = query) | 
            Q(email__icontains = query) 
        )
    
    order = request.GET.get('order')
    if order == 'asc':
        studentData = Student.objects.order_by('name')
    elif order == 'desc':
        studentData = Student.objects.order_by('-name')
    
    context = {
        "students": studentData
    }
    
    return render(request, 'student/all_student.html', context)

def update_student(request, id):

    studentData = get_object_or_404(Student, id=id)
    context = {
        'student': studentData
    }
    
    if request.method == "POST":
        studentData.name= request.POST.get('name')
        studentData.email = request.POST.get('email')
        userImage = request.FILES.get('image')
        if userImage:
            studentData.image = userImage
        studentData.save()
        return redirect('all_student')
        
    return render(request, 'student/update_student.html', context)