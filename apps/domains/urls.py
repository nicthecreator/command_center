from django.urls import path
from . import views

app_name = 'domains'

urlpatterns = [
    path('', views.DomainListView.as_view(), name='list'),
    path('novo/', views.DomainCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DomainDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.DomainUpdateView.as_view(), name='update'),
]
