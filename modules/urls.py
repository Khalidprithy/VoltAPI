from django.urls import path
from . import views

urlpatterns = [
    path('base/<int:pk>/', views.basicModel),
    path('basesearch/', views.basicModelSearch_list),
    path('basesearch/<int:pk>/', views.basicModelSearch_detail)
]
