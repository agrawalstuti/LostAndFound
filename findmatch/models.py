from django.db import models

# Create your models here.
from account.models import Account
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Lost_Person(models.Model):
    
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
    img = models.ImageField(upload_to='lost_persons')
    report = models.BooleanField(default= False)

class Lost_Item(models.Model):
    
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name='location', max_length=150)
    city = models.CharField(verbose_name='city', max_length=60)
    state = models.CharField(verbose_name='state', max_length=60)
    lost_date = models.DateField(verbose_name='lost date')
    reported_date = models.DateField(verbose_name='date reported', auto_now_add = True)
    desc = models.CharField(verbose_name='desc', max_length=255)
    img = models.ImageField(upload_to='lost_items')
    report = models.BooleanField(default= False)

class Found_Person(models.Model):
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
    img = models.ImageField(upload_to='found_persons')
    report = models.BooleanField(default= True)

class Found_Item(models.Model):
    
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name='location', max_length=150)
    city = models.CharField(verbose_name='city', max_length=60)
    state = models.CharField(verbose_name='state', max_length=60)
    found_date = models.DateField(verbose_name='found date')
    reported_date = models.DateField(verbose_name='date reported', auto_now_add = True)
    desc = models.CharField(verbose_name='desc', max_length=255)
    img = models.ImageField(upload_to='found_items')
    report = models.BooleanField(default= True)

class Success_Cases(models.Model):
    lostuser = models.ForeignKey(Account,on_delete=models.CASCADE, related_name='lost')
    founduser = models.ForeignKey(Account,on_delete=models.CASCADE, related_name='found')
    img = models.ImageField(upload_to='success_case')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    desc =  models.CharField(verbose_name='desc', max_length=255)


