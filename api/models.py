from django.db import models
from django.urls import reverse


class Status(models.Model):
    position = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class Employees(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Age')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('employee', kwargs={'employee_id': self.pk})

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Department name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'


class Organization(models.Model):
    name = models.CharField(max_length=50, verbose_name='Organization name')
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'
