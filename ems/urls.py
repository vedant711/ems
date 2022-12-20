from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('admin', views.admin, name='admin'),
    path('logout', views.logout, name='logout'),
    path('<id>', views.indi, name='dashboard'),
    path('editname/<id>', views.editname, name='editname'),
    path('editpass/<id>', views.editpass, name='editpass'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
]