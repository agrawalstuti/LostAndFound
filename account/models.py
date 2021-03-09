from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from phone_field import PhoneField
from django.core.validators import MinLengthValidator
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,firstname,lastname,address,city,state,pin,phone_no,password=None):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have username")
        if not firstname:
            raise ValueError("User must have first name")
        if not lastname:
            raise ValueError("User must have last name")
        #if not adhaar_no:
        #    raise ValueError("User must have adhaar")
        if not address:
            raise ValueError("User must provide address")
        if not city:
            raise ValueError("User must provide city name")
        if not state:
            raise ValueError("User must provide state name")
        if not pin:
            raise ValueError("User must provide pin code")
        if not phone_no:
            raise ValueError("User must have phone number")

        user = self.model(
            email= self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            #adhaar_no = adhaar_no,
            address = address,
            city = city,
            state = state,
            pin = pin,
            phone_no = phone_no
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,email,username,password,firstname,lastname,address,city,state,pin,phone_no):
        user = self.create_user(
            email= self.normalize_email(email),
            password=password,
            username = username,
            firstname = firstname,
            lastname = lastname,
            #adhaar_no = adhaar_no,
            address = address,
            city = city,
            state = state,
            pin = pin,
            phone_no = phone_no
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user




class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60, unique = True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add = True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superpower = models.BooleanField(default=False)

    firstname = models.CharField(verbose_name="first_name",max_length=30)
    lastname = models.CharField(verbose_name="last_name",max_length=30)
    #adhaar_no = models.CharField(verbose_name="adhaar",max_length=12,validators=[MinLengthValidator(10)])
    address = models.CharField(verbose_name="address",max_length=60)
    city = models.CharField(verbose_name="city",max_length=30)
    state = models.CharField(verbose_name="state",max_length=30)
    pin = models.CharField(verbose_name="pin",max_length=6, validators=[MinLengthValidator(6)])
    phone_no = models.CharField(verbose_name='contact',max_length=10,validators=[MinLengthValidator(10)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname','address','city','state','pin','phone_no']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


