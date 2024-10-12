from django.urls import path
from aplication.core import views

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [

path('', views.Home.as_view(),name='home'),
path('doctor_list/', views.DoctorList.as_view(),name='doctor_list'),
path('doctor_create/', views.DoctorCrear.as_view(),name="doctor_create"),
path('doctor_update/<int:pk>/', views.DoctorUpdate.as_view(),name='doctor_update'),
path('doctor_delete/<int:pk>/', views.DoctorDelete.as_view(),name='doctor_delete'),

]
