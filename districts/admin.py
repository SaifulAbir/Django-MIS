from django.contrib import admin

# Register your models here.
from .models import District, Division

admin.site.register(Division)
admin.site.register(District)
