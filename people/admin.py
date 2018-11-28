from django.contrib import admin
from .models import DocumentType, PersonType, Person, Phone

admin.site.register(DocumentType)
admin.site.register(PersonType)
admin.site.register(Person)
admin.site.register(Phone)
