from django.contrib import admin
from match.models import Lost_Item,Lost_Person,Found_Item,Found_Person,Category
# Register your models here.

admin.site.register(Category)

admin.site.register(Lost_Item)

admin.site.register(Lost_Person)

admin.site.register(Found_Item)

admin.site.register(Found_Person)