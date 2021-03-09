from django.shortcuts import render
from findmatch.models import Lost_Item, Lost_Person, Found_Item, Found_Person,Category
from itertools import chain
# Create your views here.
def lost_item_case(request):
    litem = Lost_Item.objects.all()
    #lperson = Lost_Person.objects.all()
    #lost_reports =list(chain(litem,lperson))
    return render(request,'lost_item_case.html',{'lost_reports':litem})

def lost_item_category(request, cname):
    cobj = Category.objects.filter(name__startswith=cname)
    cid = cobj[0].id
    litem = Lost_Item.objects.filter(category=cid)
    #lperson = Lost_Person.objects.all()
    #lost_reports =list(chain(litem,lperson))
    return render(request,'lost_item_case.html',{'lost_reports':litem})


def lost_person_case(request):
    #litem = Lost_Item.objects.all()
    lperson = Lost_Person.objects.all()
    #lost_reports =list(chain(litem,lperson))
    return render(request,'lost_person_case.html',{'lost_reports':lperson})

def lost_person_category(request, cname):
    cobj = Category.objects.filter(name__startswith=cname)
    cid = cobj[0].id
    lperson = Lost_Person.objects.filter(category=cid)
    return render(request,'lost_person_case.html',{'lost_reports':lperson})


def found_item_case(request):
    fitem = Found_Item.objects.all()
    #fperson = Found_Person.objects.all()
    #found_reports = list(chain(fitem,fperson))
    return render(request,'found_item_case.html',{'found_reports':fitem})

def found_item_category(request, cname):
    cobj = Category.objects.filter(name__startswith=cname)
    cid = cobj[0].id
    fitem = Found_Item.objects.filter(category=cid)
    return render(request,'found_item_case.html',{'found_reports':fitem})


def found_person_case(request):
    #fitem = Found_Item.objects.all()
    fperson = Found_Person.objects.all()
    #found_reports = list(chain(fitem,fperson))
    return render(request,'found_person_case.html',{'found_reports':fperson})


def found_person_category(request, cname):
    cobj = Category.objects.filter(name__startswith=cname)
    cid = cobj[0].id
    fperson = Found_Person.objects.filter(category=cid)
    return render(request,'found_person_case.html',{'found_reports':fperson})


def detail_lost_item(request,id):
    context ={}
    case = Lost_Item.objects.get(id=id)
    all_case = Lost_Item.objects.all()
    
    context['case'] = case
    context['allcase'] = all_case
    return render(request,'detail_item.html',context)


def detail_found_item(request,id):
    context ={}
    case = Found_Item.objects.get(id=id)
    all_case = Found_Item.objects.all()
    context['case'] = case
    context['allcase'] = all_case
    return render(request,'detail_item.html',context)


def detail_lost_person(request,id):
    context ={}
    case = Lost_Person.objects.get(id=id)
    all_case = Lost_Person.objects.all()
   
    context['case'] = case
    context['allcase'] = all_case
    return render(request,'detail_person.html',context)

def detail_found_person(request,id):
    context ={}
    case = Found_Person.objects.get(id=id)
    all_case = Found_Person.objects.all()
    context['case'] = case
    context['allcase'] = all_case
    return render(request,'detail_person.html',context)