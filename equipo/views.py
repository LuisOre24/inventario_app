from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import EquipoModel
from .forms import EquipoForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class EquipoView(ListView):
    model = EquipoModel
    queryset = EquipoModel.objects.all()
    template_name = 'views/equipo/equipos.html'
    context_object_name = 'equipos'

class EquipoCreate(CreateView):
    form_class = EquipoForm
    template_name = 'views/equipo/forms/create_equipo.html'
    success_url = reverse_lazy('equipo:equipo_list')

    def form_valid(self, form):
        success(self.request, 'Se registró correctamente la Equipo')
        return super().form_valid(form)

class EquipoUpdate(UpdateView):
    model = EquipoModel
    form_class = EquipoForm
    template_name = 'views/equipo/forms/update_equipo.html'
    success_url = reverse_lazy('equipo:equipo_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente la Equipo')
        return super().form_valid(form)

class EquipoDelete(DeleteView):
    model = EquipoModel
    template_name = 'views/equipo/forms/delete_equipo.html'
    success_url = reverse_lazy('equipo:equipo_list')