from django.urls import include, path
from rest_framework import routers
from .viewsets import OrganizationViewSet, DepartmentViewSet, EmployeesViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'employees', EmployeesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]