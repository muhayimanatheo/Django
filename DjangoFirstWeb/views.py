from django.shortcuts import render
from.models import *

# Create your views here.
def index(request):
    return render (request,"Homepages.html")
def signup(request):
    return render(request,"Submit.html")
def welcome(request):
    selectedData= SendM.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        message= request.POST['message']
        insertData=SendM(name=name, email=email, message=message)
        try:
            insertData.save()
            return render(request,'Welcome.html', {'message':'Data inserted!', 'data':selectedData})
        except:
            return render(request,'Welcome.html', {'message':'data does not inserted'})
    return render(request,"Welcome.html", {'data':selectedData})
def deletetodo(request, id):
    selectedData= SendM.objects.all()
    deleteData=SendM.objects.get(id=id).delete()
    return render(request,'Welcome.html',{'data':selectedData}) 