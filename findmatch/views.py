from django.shortcuts import render
from findmatch.models import *
import os
from django.core.mail import send_mail
from django.conf import settings
from skimage.metrics import structural_similarity
import imutils
import glob
import cv2
import numpy as np

# Create your views here.

def match_found_item(report_obj):
    ipath = report_obj.img.path    
    img=cv2.imread(ipath,cv2.IMREAD_GRAYSCALE)
    all_images_to_compare=[]
    titles=[]
    final={}
   
    for f in glob.glob("media/lost_items/*"):
        
        image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
        if image is None:
            continue
        print(f)
        titles.append(f)
        all_images_to_compare.append(image)
    all_images_to_compare=all_images_to_compare[:-1]

    for image_to_compare,title in zip(all_images_to_compare, titles):
        (score,diff) = structural_similarity(img,image_to_compare,full=True)
        diff=(diff*255).astype("uint8")

        final.update({title:score})
        print("Title:"+title)
        print("SSIM:{}".format(score))
    key_l=list(final.keys())
    val_l=list(final.values())
    m=((max(final.values())))
    print(m)
    p =[]
    if (m>=0.50):
        match_name=(key_l[val_l.index(m)])
        p.append(1)
        p.append(match_name)
    else:
        p.append(0) 
    print(p)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return p

def match_lost_item(report_obj):
    ipath = report_obj.img.path    
    img=cv2.imread(ipath,cv2.IMREAD_GRAYSCALE)
    all_images_to_compare=[]
    titles=[]
    final={}
    print("code worked") #a1
    for f in glob.glob("media/found_items/*"):
        print("code worked")   #a2
        image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
        if image is None:
            continue
        print(f) #a3
        titles.append(f)
        all_images_to_compare.append(image)
    #all_images_to_compare=all_images_to_compare[:-1]
    for image_to_compare,title in zip(all_images_to_compare, titles):
        (score,diff) = structural_similarity(img,image_to_compare,full=True)
        diff=(diff*255).astype("uint8")
        
        print("Title:"+title) #a3
        print("SSIM:{}".format(score)) #a4

        final.update({title:score})
    print("code worked")    #a5
    print(final) #a6
    key_l=list(final.keys()) 
    val_l=list(final.values())
    print(val_l) #a7
    m=((max(final.values())))
    print(m)   #a8
    p =[]
    if (m>=0.50):
        match_name=(key_l[val_l.index(m)])
        p.append(1)
        p.append(match_name)
    else:
        p.append(0)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(p) #a9
    return p

'''
def match_lost_item(report_obj):
    #report_obj = Found.objects.get(id=1)
    ipath = report_obj.img.path    
    img=cv2.imread(ipath,cv2.IMREAD_GRAYSCALE)
    all_images_to_compare=[]
    titles=[]
    final={}
    for f in glob.glob("media\found_items\*"):
        #print("code worked")  
        image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
        if image is None:
            continue
        #print(f)
        titles.append(f)
        all_images_to_compare.append(image)
    all_images_to_compare=all_images_to_compare[:-1]

    for image_to_compare,title in zip(all_images_to_compare, titles):
        (score,diff) = structural_similarity(img,image_to_compare,full=True)
        diff=(diff*255).astype("uint8")'''
        
        #print("Title:"+title)
        #print("SSIM:{}".format(score))
        
'''    final.update({title:score})
    #print("code worked")    
    #print(final)
    key_l=list(final.keys())
    val_l=list(final.values())
    #print(val_l)
    m=((max(final.values())))
    #print(m) 
    p =[]
    if (m>=0.50):
        match_name=(key_l[val_l.index(m)])
        p.append(1)
        p.append(match_name)
    else:
        p.append(0)    

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return p       
'''
############################

def match_lost_person(report_obj):
    ipath = report_obj.img.path    
    img=cv2.imread(ipath,cv2.IMREAD_GRAYSCALE)
    all_images_to_compare=[]
    titles=[]
    final={}
    for f in glob.glob("media/found_persons/*"):
        image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
        if image is None:
            continue
        titles.append(f)  
        print(f)
        all_images_to_compare.append(image)

    for image_to_compare,title in zip(all_images_to_compare, titles):
        (score,diff) = structural_similarity(img,image_to_compare,full=True)
        diff=(diff*255).astype("uint8")
        print("Title:"+title)
        print("SSIM:{}".format(score))
        final.update({title:score}) 
    #print(final)
    key_l=list(final.keys())
    val_l=list(final.values())
    #print(val_l)
    m=((max(final.values())))
    print(m) 
    p = []
    if (m>=0.27):
        match_name=(key_l[val_l.index(m)])
        p.append(1)
        p.append(match_name)
    else:
        p.append(0)   
    print(p) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return p



def match_found_person(report_obj):
    ipath = report_obj.img.path    
    img=cv2.imread(ipath,cv2.IMREAD_GRAYSCALE)
    all_images_to_compare=[]
    titles=[]
    final={}
    #print("before loop")
    for f in glob.glob("media/lost_persons/*"):
        image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
        if image is None:
            continue
        titles.append(f)
        print(f)
        all_images_to_compare.append(image)
    #print("after loop")
    for image_to_compare,title in zip(all_images_to_compare, titles):
        (score,diff) = structural_similarity(img,image_to_compare,full=True)
        diff=(diff*255).astype("uint8")
        print("Title:"+title)
        print("SSIM:{}".format(score))
        final.update({title:score})
    #print(final)
    key_l=list(final.keys())
    val_l=list(final.values())
    #print(val_l)
    m=((max(final.values())))
    print(m) 
    p = []
    if (m>=0.27):
        match_name=(key_l[val_l.index(m)])
        p.append(1)
        p.append(match_name)
    else:
        p.append(0) 
    print(p)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return p

##################

def rename(report_obj):
    initial_path = report_obj.img.path
    name = report_obj.img.name
    lst = name.split('/')
    ext = lst[-1].split('.')[-1]
    update_to = str(report_obj.pk)+'.'+ext
    new_name = lst[0]+'/'+update_to
    report_obj.img.name = new_name
    new_path = os.path.join(settings.MEDIA_ROOT , report_obj.img.name)
    os.rename(initial_path,new_path)
    report_obj.save()
    return    

def message(request,msg):

    return render(request,'message.html',{'msg':msg})


def lost_item(request):
    
    if request.method=="POST":
        category=request.POST['Category']
        location = request.POST['location']
        city = request.POST['city']
        state = request.POST['state']
        lost_date =request.POST['date']
        img=request.FILES['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        lost_item_obj = Lost_Item(user = request.user,category=category_obj,location=location,city=city,
            state=state,lost_date=lost_date,desc=desc,img=img, report=False)
        lost_item_obj.save()
        rename(lost_item_obj)
        print("Report has been filed")
        p = []
        p = match_lost_item(lost_item_obj)
        if p[0] == 0:
            msg = 'Match has not been found'
            print(msg)
        else:
            msg = 'Match has been found'
            print(msg)
            print(p[1])
            img_address = p[1].split('.')[0]
            print(img_address)
            report_id = img_address.split('\\')[-1]
            print(report_id)
            user1 = request.user
            found_item_obj = Found_Item.objects.get(id=report_id)
            user2 = found_item_obj.user
            #user1 = Account.objects.get(id = user1_id)
            send_mail(
                'Match has been Found',
                'Report that you have filed about missing item on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly verify the match and complete further process. Kindly Lost And Found team',
                'sa.stutiagrawal@example.com',
                [user1.email],
                fail_silently=False,
            )
            send_mail(
                'Match has been Found',
                'Report that you have filed about unknown found item on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly look forward to it. Kindly Lost And Found Team',
                'sa.stutiagrawal@example.com',
                [user2.email],
                fail_silently=False,
            )
            match = Success_Cases(lostuser = user1, founduser = user2, img = img, category= category_obj, desc= desc)
            match.save()
            rename(match)
            print("success object has been created")
            found_item_obj.img.delete()
            found_item_obj.delete()
            lost_item_obj.img.delete()
            lost_item_obj.delete()
            send_mail(
                'Match has been Found',
                'Please verify for the success report whose id is '+ str(match.pk) +
                'and report it to the user',
                'sa.stutiagrawal@example.com',
                ['sa.stutiagrawal@gmail.com'],
                fail_silently=False,
            )
            msg = msg +' please note this id for reference purpose - '+ str(match.pk)
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
        img=request.FILES['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        lost_person_obj = Lost_Person(user = request.user,category=category_obj,location=location,city=city,
            state=state,name=name,age=age,lost_date=lost_date,desc=desc,img=img, report=False)
        lost_person_obj.save()
        rename(lost_person_obj)
        p = []
        p = match_lost_person(lost_person_obj)
        if p[0] == 0:
            msg = 'Match has not been found'
        else:
            msg = 'Match has been found'
            print(p[1])
            img_address = p[1].split('.')[0]
            print(img_address)
            #report_id = img_address[-1]
            report_id = img_address.split('\\')[-1]
            print(report_id)
            user1 = request.user
            found_person_obj = Found_Person.objects.get(id=report_id)
            user2 = found_person_obj.user
            #user1 = Account.objects.get(id = user1_id)
            send_mail(
                'Match has been Found',
                'Report that you have filed about missing person on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly verify the match and complete further process. Kindly Lost And Found team',
                'sa.stutiagrawal@example.com',
                [user1.email],
                fail_silently=False,
            )
            send_mail(
                'Match has been Found',
                'Report that you have filed about unknown person on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly look forward to it. Kindly Lost And Found Team',
                'sa.stutiagrawal@example.com',
                [user2.email],
                fail_silently=False,
            )
            match = Success_Cases(lostuser = user1, founduser = user2, img = img, category= category_obj, desc= desc)
            match.save()
            rename(match)
            print("success object has been created")
            found_person_obj.img.delete()
            found_person_obj.delete()
            lost_person_obj.img.delete()
            lost_person_obj.delete()
            send_mail(
                'Match has been Found',
                'Please verify for the success report whose id is '+ str(match.pk) +
                'and report it to the user',
                'sa.stutiagrawal@example.com',
                ['sa.stutiagrawal@gmail.com'],
                fail_silently=False,
            )
            msg = msg +' please note this id for reference purpose - '+ str(match.pk)
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
        img=request.FILES['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        found_item_obj = Found_Item(user = request.user,category=category_obj,location=location,city=city,
            state=state,found_date=found_date,desc=desc,img=img, report=True)
        found_item_obj.save()
        rename(found_item_obj)
        
        p = []
        p = match_found_item(found_item_obj)
        if p[0] == 0:
            msg = 'Match has not been found'
        else:
            msg = 'Match has been found'
            print(p[1])
            img_address = p[1].split('.')[0]
            print(img_address)
            #report_id = img_address[-1]
            report_id = img_address.split('\\')[-1]
            print(report_id)
            user2 = request.user
            lost_item_obj = Lost_Item.objects.get(id=report_id)
            user1 = lost_item_obj.user
            #user1 = Account.objects.get(id = user1_id)
            send_mail(
                'Match has been Found',
                'Report that you have filed about missing item on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly verify the match and complete further process. Kindly Lost And Found team',
                'sa.stutiagrawal@example.com',
                [user1.email],
                fail_silently=False,
            )
            send_mail(
                'Match has been Found',
                'Report that you have filed about unknown found item on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly look forward to it. Kindly Lost And Found Team',
                'sa.stutiagrawal@example.com',
                [user2.email],
                fail_silently=False,
            )
            match = Success_Cases(lostuser = user1, founduser = user2, img = img, category= category_obj, desc= desc)
            match.save()
            rename(match)
            print("success object has been created")
            found_item_obj.img.delete()
            found_item_obj.delete()
            lost_item_obj.img.delete()
            lost_item_obj.delete()
            send_mail(
                'Match has been Found',
                'Please verify for the success report whose id is '+ str(match.pk) +
                'and report it to the user',
                'sa.stutiagrawal@example.com',
                ['sa.stutiagrawal@gmail.com'],
                fail_silently=False,
            )
            msg = msg +' please note this id for reference purpose - '+ str(match.pk)
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
        img=request.FILES['file_1']
        desc=request.POST['desc']
        category_obj = Category.objects.get(name=category)
        found_person_obj = Found_Person(user = request.user,category=category_obj,location=location,city=city,
            state=state,name=name,age=age,found_date=found_date,desc=desc,img=img, report=True)
        found_person_obj.save()
        rename(found_person_obj)
        p = []
        p = match_found_person(found_person_obj)
        if p[0] == 0:
            msg = 'Match has not been found'
        else:
            msg = 'Match has been found'
            print(p[1])
            img_address = p[1].split('.')[0]
            print(img_address)
            report_id = img_address.split('\\')[-1]
            #report_id = img_address[-1]
            print(report_id)
            user2 = request.user
            lost_person_obj = Lost_Person.objects.get(id=report_id)
            user1 = lost_person_obj.user
            #user1 = Account.objects.get(id = user1_id)
            send_mail(
                'Match has been Found',
                'Report that you have filed about missing person on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly verify the match and complete further process. Kindly Lost And Found team',
                'sa.stutiagrawal@example.com',
                [user1.email],
                fail_silently=False,
            )
            send_mail(
                'Match has been Found',
                'Report that you have filed about unknown person on our website Lost And Found. We are glad to inform '+ 
                'you that match has been found . We request you kindly look forward to it. Kindly Lost And Found Team',
                'sa.stutiagrawal@example.com',
                [user2.email],
                fail_silently=False,
            )
            match = Success_Cases(lostuser = user1, founduser = user2, img = img, category= category_obj, desc= desc)
            match.save()
            rename(match)
            print("success object has been created")
            found_person_obj.img.delete()
            found_person_obj.delete()
            lost_person_obj.img.delete()
            lost_person_obj.delete()
            send_mail(
                'Match has been Found',
                'Please verify for the success report whose id is '+ str(match.pk) +
                'and report it to the user',
                'sa.stutiagrawal@example.com',
                ['sa.stutiagrawal@gmail.com'],
                fail_silently=False,
            )
            msg = msg +' please note this id for reference purpose - '+ str(match.pk)
        return render(request,'message.html',{'msg':msg})
    else:
        return render(request,'found_person.html')