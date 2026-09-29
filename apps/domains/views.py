from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Domain
from .forms import DomainForm

class DomainListView(LoginRequiredMixin, ListView):
    model = Domain
    template_name = 'domains/domains_list.html'
    context_object_name = 'domains'
    paginate_by = 10

class DomainDetailView(LoginRequiredMixin, DetailView):
    model = Domain
    template_name = 'domains/domains_detail.html'
    context_object_name = 'domain'
    
class DomainCreateView(LoginRequiredMixin, CreateView):
    model = Domain
    template_name = 'domains/domains_form.html'
    form_class = DomainForm
    
    def get_success_url(self):
        return reverse_lazy('domains:detail', kwargs={'pk': self.object.pk})

class DomainUpdateView(LoginRequiredMixin, UpdateView):
    model = Domain
    template_name = 'domains/domains_form.html'
    form_class = DomainForm
    
    def get_success_url(self):
        return reverse_lazy('domains:detail', kwargs={'pk': self.object.pk})
