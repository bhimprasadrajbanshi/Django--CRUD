from django.urls import path,include
from crud import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:Employees_id>', views.delete, name='delete'),
]