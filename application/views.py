from multiprocessing import context
from django.shortcuts import render
from .models import drugs
from .form import drugsform
from .models import drugs




def Home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        data=drugs.objects.filter(name__icontains=q)
    else:

     data=drugs.objects.all().order_by('id')
    
    context={
     'data':data
    }
    return render(request,'pages/Home.html',context)

def signup(request):
    data= drugsform(request.POST, request.FILES)
    if data.is_valid():
        data.save()
    else:
        print("Not valid")
    return render(request, 'pages/signup.html', {"form": drugsform})



def deletewithid(request, id):
    data = drugs.objects.get(pk=id)
   
    data.delete()
    data = drugs.objects.all().order_by('id')
    dict = {"data": data}
    return render(request, 'pages/Home.html ', dict)


def update(request,id):
    data=drugs.objects.get(id=id)
    if request.method =='POST':
     data_save=drugsform(request.POST, request.FILES,instance=data)
     if data_save.is_valid():
        data_save.save()
    else:
        data_save=drugsform(instance=data)

    context={

        'form':data_save,
    }
    return render(request,'pages/update.html',context)