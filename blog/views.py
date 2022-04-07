from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html')



def Login(request):
    return render (request,'login.html')

def Profile(request):
    return render(request,'profile.html')
