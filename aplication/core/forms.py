from django import forms

from aplication.core.models import Doctor, Medicamento, License

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


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['doctor', 'license_number', 'issued_date']
        widgets = {
            'issued_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }, format='%Y-%m-%d'
            ),
        }
        labels = {
            'doctor': 'Doctor',
            'license_number': 'Número de Licencia',
            'issued_date': 'Fecha de Emisión',
        }