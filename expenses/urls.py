from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('register/', views.register, name='register'),
]
