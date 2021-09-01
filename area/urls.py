from django.urls import path
from .views import AreaView,AreaCreate, AreaUpdate, AreaDelete

urlpatterns = [
    path('areas/', AreaView.as_view(), name='area_list'),
    path('areas/create', AreaCreate.as_view(), name='create_area'),
    path('areas/update/<pk>', AreaUpdate.as_view(), name='update_area'),
    path('areas/delete/<pk>', AreaDelete.as_view(), name='delete_area'),
]