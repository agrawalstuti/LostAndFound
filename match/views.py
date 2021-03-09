from django.shortcuts import render
from match.models import Category,Lost_Item,Lost_Person,Found_Item,Found_Person
# Create your views here.
def message(request,msg):

    return render(request,'message.html',{'msg':msg})


def lost_item(request):
    
    if request.method=="POST":
        category=request.POST['Category']
        location = request.POST['location']
        city = request.POST['city']
        state = request.POST['state']
        lost_date =request.POST['date']
        img=request.POST['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        lost_item_obj = Lost_Item(user = request.user,category=category_obj,location=location,city=city,
            state=state,lost_date=lost_date,desc=desc,img=img)
        lost_item_obj.save()
        msg = 'Report has been filed'
        return render(request,'message.html',{'msg':msg})
    else:
        return render(request,'lost_item.html')

def lost_person(request):
    if request.method=="POST":
        category=request.POST['Category']
        location = request.POST['location']
        city = request.POST['city']
        state = request.POST['state']
        name = request.POST['lost_name']
        age = request.POST['age']
        lost_date =request.POST['date']
        img=request.POST['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        lost_person_obj = Lost_Person(user = request.user,category=category_obj,location=location,city=city,
            state=state,name=name,age=age,lost_date=lost_date,desc=desc,img=img)
        lost_person_obj.save()
        msg = 'Report has been filed'
        return render(request,'message.html',{'msg':msg})
    else:
        return render(request,'lost_person.html')
    
def found_item(request):
    if request.method=="POST":
        category=request.POST['Category']
        location = request.POST['location']
        city = request.POST['city']
        state = request.POST['state']
        found_date =request.POST['date']
        img=request.POST['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        found_item_obj = Found_Item(user = request.user,category=category_obj,location=location,city=city,
            state=state,found_date=lost_date,desc=desc,img=img)
        found_item_obj.save()
        msg = 'Report has been filed'
        return render(request,'message.html',{'msg':msg})
    else:
        return render(request,'found_item.html')
    
def found_person(request):
    if request.method=="POST":
        category=request.POST['Category']
        location = request.POST['location']
        city = request.POST['city']
        state = request.POST['state']
        name = request.POST['found_name']
        age = request.POST['age']
        found_date =request.POST['date']
        img=request.POST['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        lost_item_obj = Found_Person(user = request.user,category=category_obj,location=location,city=city,
            state=state,name=name,age=age,found_date=lost_date,desc=desc,img=img)
        lost_item_obj.save()
        msg = 'Report has been filed'
        return render(request,'message.html',{'msg':msg})
    else:
        return render(request,'found_person.html')