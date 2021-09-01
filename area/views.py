from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import AreaModel
from .forms import AreaForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class AreaView(ListView):
    model = AreaModel
    queryset = AreaModel.objects.all()
    template_name = 'views/area/areas.html'
    context_object_name = 'areas'

class AreaCreate(CreateView):
    form_class = AreaForm
    template_name = 'views/area/forms/create_area.html'
    success_url = reverse_lazy('area:area_list')

    def form_valid(self, form):
        success(self.request, 'Se registró correctamente la Area')
        return super().form_valid(form)

class AreaUpdate(UpdateView):
    model = AreaModel
    form_class = AreaForm
    template_name = 'views/area/forms/update_area.html'
    success_url = reverse_lazy('area:area_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente la Area')
        return super().form_valid(form)

class AreaDelete(DeleteView):
    model = AreaModel
    template_name = 'views/area/forms/delete_area.html'
    success_url = reverse_lazy('area:area_list')
