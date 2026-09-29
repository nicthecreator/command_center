from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import MaintenanceContract
from .forms import MaintenanceContractForm

class MaintenanceContractListView(LoginRequiredMixin, ListView):
    model = MaintenanceContract
    template_name = 'maintenance/maintenance_list.html'
    context_object_name = 'maintenance'
    paginate_by = 10

class MaintenanceContractDetailView(LoginRequiredMixin, DetailView):
    model = MaintenanceContract
    template_name = 'maintenance/maintenance_detail.html'
    context_object_name = 'maintenanc'
    
class MaintenanceContractCreateView(LoginRequiredMixin, CreateView):
    model = MaintenanceContract
    template_name = 'maintenance/maintenance_form.html'
    form_class = MaintenanceContractForm
    
    def get_success_url(self):
        return reverse_lazy('maintenance:detail', kwargs={'pk': self.object.pk})

class MaintenanceContractUpdateView(LoginRequiredMixin, UpdateView):
    model = MaintenanceContract
    template_name = 'maintenance/maintenance_form.html'
    form_class = MaintenanceContractForm
    
    def get_success_url(self):
        return reverse_lazy('maintenance:detail', kwargs={'pk': self.object.pk})
