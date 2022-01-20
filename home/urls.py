from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('test/', views.test_page, name='test'),
    path('<int:id>/', views.update_data, name='update'),
]
