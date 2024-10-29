from django.shortcuts import render,redirect
from myapp.forms import RegisterForm
from myapp.models import Register

# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

        else:
            print("Please Check your entry properly")
    context = {'form':form}
    return render(request,"myapp/register.html",context=context)
