from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from aplication.core.forms import DoctorForm
from aplication.core.models import Doctor


class Home(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Sistema Medico Online"
        return context


class DoctorList(ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Doctores"
        return context

class DoctorCrear(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')

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


class DoctorUpdate(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')

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


class DoctorDelete(DeleteView):
    model = Doctor
    template_name = 'core/doctor/delete.html'
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar"
        context['title1'] = "Eliminar Doctor"
        return context

