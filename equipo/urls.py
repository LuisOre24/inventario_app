from django.urls import path
from .views import EquipoView,EquipoCreate, EquipoUpdate, EquipoDelete

urlpatterns = [
    path('equipos/', EquipoView.as_view(), name='equipo_list'),
    path('equipos/create', EquipoCreate.as_view(), name='create_equipo'),
    path('equipos/update/<pk>', EquipoUpdate.as_view(), name='update_equipo'),
    path('equipos/delete/<pk>', EquipoDelete.as_view(), name='delete_equipo'),
]