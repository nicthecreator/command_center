from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.ClientListView.as_view(), name='list'),
    path('novo/', views.ClientCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ClientDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.ClientUpdateView.as_view(), name='update'),
]
