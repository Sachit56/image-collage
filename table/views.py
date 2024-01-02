from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
def HomeView(request):
    if request.POST:
     form=ImageForm(request.POST,request.FILES)

     if form.is_valid():
        form.save()
    #  else:
    #     print(form.errors)   
    # else:
    #    form=ImageForm()   
    form=ImageForm()     

    return render(request,'table/home.html',{
        'form':form
    })