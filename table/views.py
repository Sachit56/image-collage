from django.shortcuts import render
from .forms import ImageForm
from .models import ImageModel

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
    img= ImageModel.objects.all()

    return render(request,'table/home.html',{
        'form':form,
        'img':img
    })