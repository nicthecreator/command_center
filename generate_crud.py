import os

def generate_crud(app_name, model_name, fields_list):
    base_dir = f"apps/{app_name}"
    
    # urls.py
    urls_content = f"""from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
    path('', views.{model_name}ListView.as_view(), name='list'),
    path('novo/', views.{model_name}CreateView.as_view(), name='create'),
    path('<int:pk>/', views.{model_name}DetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.{model_name}UpdateView.as_view(), name='update'),
]
"""
    with open(f"{base_dir}/urls.py", "w", encoding='utf-8') as f:
        f.write(urls_content)
        
    # forms.py
    fields_str = ', '.join([f"'{f}'" for f in fields_list])
    forms_content = f"""from django import forms
from .models import {model_name}

class {model_name}Form(forms.ModelForm):
    class Meta:
        model = {model_name}
        fields = [{fields_str}]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            else:
                field.widget.attrs['class'] = 'w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
"""
    with open(f"{base_dir}/forms.py", "w", encoding='utf-8') as f:
        f.write(forms_content)
        
    # views.py
    views_content = f"""from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import {model_name}
from .forms import {model_name}Form

class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{app_name}/{app_name}_list.html'
    context_object_name = '{app_name}'
    paginate_by = 10

class {model_name}DetailView(DetailView):
    model = {model_name}
    template_name = '{app_name}/{app_name}_detail.html'
    context_object_name = '{app_name[:-1]}'
    
class {model_name}CreateView(CreateView):
    model = {model_name}
    template_name = '{app_name}/{app_name}_form.html'
    form_class = {model_name}Form
    
    def get_success_url(self):
        return reverse_lazy('{app_name}:detail', kwargs={{'pk': self.object.pk}})

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    template_name = '{app_name}/{app_name}_form.html'
    form_class = {model_name}Form
    
    def get_success_url(self):
        return reverse_lazy('{app_name}:detail', kwargs={{'pk': self.object.pk}})
"""
    with open(f"{base_dir}/views.py", "w", encoding='utf-8') as f:
        f.write(views_content)
        
    # Ensure templates dir exists
    os.makedirs(f"{base_dir}/templates/{app_name}", exist_ok=True)
    
generate_crud('finance', 'Sale', ['project', 'client', 'amount', 'sale_date', 'status', 'notes'])
generate_crud('maintenance', 'MaintenanceContract', ['project', 'client', 'active', 'monthly_value', 'start_date', 'next_billing_date', 'description', 'notes'])

print("CRUD skeleton generated for domains and hosting.")
