from django.contrib import admin
from .models import Company
from .models import City
from .models import Brand

admin.site.register(Company)
admin.site.register(City)
admin.site.register(Brand)
