from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Project
from django.db.models import Q

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtros de Busca Simples
        q = self.request.GET.get('q')
        status = self.request.GET.get('status')
        category = self.request.GET.get('category')
        
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | 
                Q(client__name__icontains=q)
            )
        if status:
            queryset = queryset.filter(status=status)
        if category:
            queryset = queryset.filter(category_id=category)
            
        return queryset

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

from .forms import ProjectForm

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'slug': self.object.slug})

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'slug': self.object.slug})
