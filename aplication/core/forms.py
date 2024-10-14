from django import forms

from aplication.core.models import Doctor, Medicamento

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['first_name','last_name','profession','clinic','sex','birth_date','address','is_active']
        

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(),
        }
