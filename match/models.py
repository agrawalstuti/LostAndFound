from django.db import models
from account.models import Account
from django.conf import settings
# Create your models here.
#Logic to rename image with primary key while uploading in database
from django.utils import timezone
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible 
class UploadToPathAndRename(object):

    def __init__(self,path):
        self.sub_path = path

    def __call__(self,instance,filename):
        ext = filename.split('.')[-1]
        #get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk,ext)
        else:
            filename = '{}.{}'.format(uuid4().hex,ext)
        return os.path.join(self.sub_path,filename)




class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Lost_Person(models.Model):
    #global store_at ,main_id, lostp_id
    #store_at = 'lost_person'
    #lostp_id+=1
    #main_id = lostp_id
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name='location', max_length=150)
    city = models.CharField(verbose_name='city', max_length=60)
    state = models.CharField(verbose_name='state', max_length=60)
    name = models.CharField(verbose_name='name',max_length=60)
    age = models.IntegerField(verbose_name='age')
    lost_date = models.DateField(verbose_name='lost date')
    reported_date = models.DateField(verbose_name='date reported', auto_now_add = True)
    desc = models.CharField(verbose_name='desc', max_length=255)
    img = models.ImageField(upload_to='lperson')

class Lost_Item(models.Model):
    #global store_at, main_id, losti_id
    #store_at = 'lost_item'
    #losti_id+=1
    #main_id = losti_id
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name='location', max_length=150)
    city = models.CharField(verbose_name='city', max_length=60)
    state = models.CharField(verbose_name='state', max_length=60)
    lost_date = models.DateField(verbose_name='lost date')
    reported_date = models.DateField(verbose_name='date reported', auto_now_add = True)
    desc = models.CharField(verbose_name='desc', max_length=255)
    img = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(settings.MEDIA_ROOT,'lost_item')))

class Found_Person(models.Model):
    #global store_at, main_id, foundp_id
    #store_at = 'found_person'
    #foundp_id+=1
    #main_id = foundp_id
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name='location', max_length=150)
    city = models.CharField(verbose_name='city', max_length=60)
    state = models.CharField(verbose_name='state', max_length=60)
    name = models.CharField(verbose_name='name',max_length=60, null=True, blank=True)
    age = models.IntegerField(verbose_name='age')
    found_date = models.DateField(verbose_name='found date')
    reported_date = models.DateField(verbose_name='date reported', auto_now_add = True)
    desc = models.CharField(verbose_name='desc', max_length=255)
    img = models.ImageField(upload_to='fperson')

class Found_Item(models.Model):
    #global store_at, main_id, foundi_id
    #store_at = 'found_item'
    #foundi_id+=1
    #main_id = foundi_id
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name='location', max_length=150)
    city = models.CharField(verbose_name='city', max_length=60)
    state = models.CharField(verbose_name='state', max_length=60)
    found_date = models.DateField(verbose_name='found date')
    reported_date = models.DateField(verbose_name='date reported', auto_now_add = True)
    desc = models.CharField(verbose_name='desc', max_length=255)
    img = models.ImageField(upload_to='fitem')

