from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('position',)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'department', 'status')
    list_display_links = ('first_name', 'last_name', )
    search_fields = ('first_name', 'last_name', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', )

