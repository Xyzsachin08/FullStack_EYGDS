from django.urls import path
from . import views

urlpatterns = [
    path('', views.mobile_form, name='insert'),
    path('<int:id>/', views.mobile_form, name='update'),
    path('list/', views.mobile_list, name='list'),
    path('delete/<int:id>/', views.mobile_delete, name='delete'),
]