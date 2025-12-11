from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

# def add_student(request):
#     if request.method == "POST":
        