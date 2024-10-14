from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from aplication.core.forms import DoctorForm, MedicamentoForm
from aplication.core.models import Doctor, Medicamento



################################################################
# Registro de usuario
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('core:home')  # Redirige a la página principal después del registro

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# Iniciar sesión
class SignInView(LoginView):
    template_name = 'registration/signin.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True  # Redirige al usuario autenticado si ya ha iniciado sesión

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# Cerrar sesión
class SignOutView(LogoutView):
    next_page = reverse_lazy('core:home')  # Redirige a la página principal después de cerrar sesión



################################################################
# Home
class Home(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Sistema Medico Online"
        return context

# Lista de Doctores (solo accesible si se ha iniciado sesión)
class DoctorList(ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctores'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Doctores"
        return context

# Crear Doctor
class DoctorCrear(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Doctores"
        context['title1'] = "Añadir Doctores"
        return context

    def form_invalid(self, form):
        context = self.get_context_data()
        context['form'] = form
        context['error'] = "Error al crear el Doctor."
        return self.render_to_response(context)

# Actualizar Doctor
class DoctorUpdate(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Doctores"
        context['title1'] = "Editar Doctor"
        return context

    def form_invalid(self, form):
        context = self.get_context_data()
        context['form'] = form
        context['error'] = "Error al editar el Doctor."
        return self.render_to_response(context)

# Eliminar Doctor
class DoctorDelete(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'core/doctor/delete.html'
    success_url = reverse_lazy('core:doctor_list')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar"
        context['title1'] = "Eliminar Doctor"
        return context

################################################################

class MedicamentoList( ListView):
    model = Medicamento
    template_name = 'core/medicamento/list.html'
    context_object_name = 'medic'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Consulta Medicamentos"
        return context


class MedicamentoCreate(LoginRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('core:medicamento_list')
    login_url = 'core:login'

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asignar el usuario actual
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Medicamento"
        return context


class MedicamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('core:medicamento_list')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Medicamento"
        return context


class MedicamentoDelete(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name = 'core/medicamento/delete.html'
    success_url = reverse_lazy('core:medicamento_list')
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Medicamento"
        return context
