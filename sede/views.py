from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import SedeModel
from .forms import SedeForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

#class MyView(View):
#
#    def get(self, request, *args, **kwargs):
#        suma = 5 + 7
#        print(suma)
#        return HttpResponse('<b>Vamos a conquistar al delmer yo luis ore</b>')


class SedeView(ListView):
    model = SedeModel
    queryset = SedeModel.objects.all()
    template_name = 'views/sede/sedes.html'
    context_object_name = 'sedes'

class SedeCreate(CreateView):
    form_class = SedeForm
    template_name = 'views/sede/forms/create_sede.html'
    success_url = reverse_lazy('sede:sede_list')

    def form_valid(self, form):
        success(self.request, 'Se registró correctamente la Sede')
        return super().form_valid(form)

class SedeUpdate(UpdateView):
    model = SedeModel
    form_class = SedeForm
    template_name = 'views/sede/forms/update_sede.html'
    success_url = reverse_lazy('sede:sede_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente la Sede')
        return super().form_valid(form)

class SedeDelete(DeleteView):
    model = SedeModel
    template_name = 'views/sede/forms/delete_sede.html'
    success_url = reverse_lazy('sede:sede_list')
