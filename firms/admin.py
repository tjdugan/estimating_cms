from django.contrib import admin

from .models import Architect, Contractor, Manufacturer, ProductRep, ProjectManager, Salesman, Supplier

# Register your models here.
admin.site.register(Contractor)
admin.site.register(ProjectManager)
admin.site.register(Architect)
admin.site.register(Supplier)
admin.site.register(Salesman)
admin.site.register(Manufacturer)
admin.site.register(ProductRep)