from django.urls import path
from aplication.core import views

app_name = 'core'  # Define un espacio de nombres para la aplicación

urlpatterns = [
    # Ruta a la página principal
    path('', views.Home.as_view(), name='home'),
    
    # Rutas para la gestión de doctores
    path('doctor_list/', views.DoctorList.as_view(), name='doctor_list'),
    path('doctor_create/', views.DoctorCrear.as_view(), name="doctor_create"),
    path('doctor_update/<int:pk>/', views.DoctorUpdate.as_view(), name='doctor_update'),
    path('doctor_delete/<int:pk>/', views.DoctorDelete.as_view(), name='doctor_delete'),
    
    # Rutas para el sistema de autenticación
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.SignInView.as_view(), name='login'),
    # urls.py
    path('logout/', views.SignOutView.as_view(), name='logout'),
    
    
    # Rutas para la gestión de medicamentos
    path('medicamento/', views.MedicamentoList.as_view(), name='medicamento_list'),
    path('medicamento/create/', views.MedicamentoCreate.as_view(), name='medicamento_create'),
    path('medicamento/update/<int:pk>/', views.MedicamentoUpdate.as_view(), name='medicamento_update'),
    path('medicamento/delete/<int:pk>/', views.MedicamentoDelete.as_view(), name='medicamento_delete'),
    # Otras rutas
    
    # Rutas para la gestión de licencias
    path('license/', views.LicenseList.as_view(), name='license_list'),
    path('license/create/', views.LicenseCreate.as_view(), name='license_create'),
    path('license/update/<int:pk>/', views.LicenseUpdate.as_view(), name='license_update'),
    path('license/delete/<int:pk>/', views.LicenseDelete.as_view(), name='license_delete'),

]
