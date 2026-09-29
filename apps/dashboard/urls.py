from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('monitoramento/', views.monitoring_view, name='monitoring'),
    path('alertas/', views.alerts_view, name='alerts'),
    path('configuracoes/', views.settings_view, name='settings'),
]
