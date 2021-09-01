from django.urls import path
from .views import SedeView,SedeCreate, SedeUpdate, SedeDelete

urlpatterns = [
    path('sedes/', SedeView.as_view(), name='sede_list'),
    path('sedes/create', SedeCreate.as_view(), name='create_sede'),
    path('sedes/update/<pk>', SedeUpdate.as_view(), name='update_sede'),
    path('sedes/delete/<pk>', SedeDelete.as_view(), name='delete_sede'),
]