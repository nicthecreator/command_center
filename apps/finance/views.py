from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Sale
from .forms import SaleForm

class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'finance/finance_list.html'
    context_object_name = 'finance'
    paginate_by = 10

class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'finance/finance_detail.html'
    context_object_name = 'financ'
    
class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    template_name = 'finance/finance_form.html'
    form_class = SaleForm
    
    def get_success_url(self):
        return reverse_lazy('finance:detail', kwargs={'pk': self.object.pk})

class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model = Sale
    template_name = 'finance/finance_form.html'
    form_class = SaleForm
    
    def get_success_url(self):
        return reverse_lazy('finance:detail', kwargs={'pk': self.object.pk})
