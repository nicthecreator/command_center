from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.SaleListView.as_view(), name='list'),
    path('novo/', views.SaleCreateView.as_view(), name='create'),
    path('<int:pk>/', views.SaleDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.SaleUpdateView.as_view(), name='update'),
]
