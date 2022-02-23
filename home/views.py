from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("This is the about us page")

def Products(request):
    return HttpResponse("This is the our products page")

def login(request):
    return HttpResponse("This is the login\signup page")
    