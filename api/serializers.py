from rest_framework import serializers

from api.models import Organization, Department, Employees


class OrganizationSerializer(serializers.ModelSerializer):
    departments_count = serializers.SerializerMethodField()
    employees_count = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ('name', 'departments_count', 'employees_count')

    def get_departments_count(self, obj):
        return obj.departments.count()

    def get_employees_count(self, obj):
        return Employees.objects.filter(department__in=obj.departments.values_list('pk', flat=True)).count()


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('name', 'employees_count')

    def get_employees_count(self, obj):
        return Employees.objects.filter(department_id=obj.id).count()


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
