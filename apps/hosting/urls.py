from django.urls import path
from . import views

app_name = 'hosting'

urlpatterns = [
    path('', views.HostingAccountListView.as_view(), name='list'),
    path('novo/', views.HostingAccountCreateView.as_view(), name='create'),
    path('<int:pk>/', views.HostingAccountDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.HostingAccountUpdateView.as_view(), name='update'),
]
