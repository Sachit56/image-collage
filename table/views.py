from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request,'table/home.html')