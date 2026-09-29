from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.MaintenanceContractListView.as_view(), name='list'),
    path('novo/', views.MaintenanceContractCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MaintenanceContractDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.MaintenanceContractUpdateView.as_view(), name='update'),
]
