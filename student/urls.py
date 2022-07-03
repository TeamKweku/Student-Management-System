from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  
    path('<int:id>/', views.view_student, name='view-student'),
    path('add/', views.add_student, name='add-student'),
]