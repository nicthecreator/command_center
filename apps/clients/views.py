from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Client
from .forms import ClientForm
from django.db.models import Q

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        
        q = self.request.GET.get('q')
        is_active = self.request.GET.get('is_active')
        
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | 
                Q(company_name__icontains=q) |
                Q(email__icontains=q)
            )
        
        if is_active == 'true':
            queryset = queryset.filter(is_active=True)
        elif is_active == 'false':
            queryset = queryset.filter(is_active=False)
            
        return queryset

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contexto extra com os projetos do cliente (já disponíveis via reverse relation related_name='projects')
        # Mas podemos garantir a ordenação aqui se precisarmos
        context['client_projects'] = self.object.projects.all().order_by('-created_at') if hasattr(self.object, 'projects') else []
        return context

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'clients/client_form.html'
    form_class = ClientForm
    
    def get_success_url(self):
        return reverse_lazy('clients:detail', kwargs={'pk': self.object.pk})

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'clients/client_form.html'
    form_class = ClientForm
    
    def get_success_url(self):
        return reverse_lazy('clients:detail', kwargs={'pk': self.object.pk})
