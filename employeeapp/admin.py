from django.contrib import admin

from employeeapp.models import Employee,Qualification,workExperience,AddressDetails,projects
# Register your models here.

admin.site.register(Employee)
admin.site.register(Qualification)
admin.site.register(workExperience)
admin.site.register(AddressDetails)
admin.site.register(projects)
