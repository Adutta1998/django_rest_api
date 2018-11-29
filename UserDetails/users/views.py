from django.shortcuts import render,HttpResponse
from .models import UserData

# Create your views here.
def AddData(request):
    return render(request,'index.html')

def DataSubmit(request):
    if(request.method == 'POST'):
        fname = request.POST['fname']
        lname = request.POST['lname']
        adrs = request.POST['adrs']
        dob = request.POST['dob']
        wght = request.POST['wght']
        hght = request.POST['hght']
        bld_grp = request.POST['bld_grp']
        model = UserData(first_name=fname,last_name=lname,dob=dob,address=adrs,height=hght,weight=wght,blood_grp=bld_grp)
        model.save()
        return HttpResponse(request.POST['fname'])
    else:
        return render(request,'index.html')