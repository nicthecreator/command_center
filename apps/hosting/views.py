from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import HostingAccount
from .forms import HostingAccountForm

class HostingAccountListView(LoginRequiredMixin, ListView):
    model = HostingAccount
    template_name = 'hosting/hosting_list.html'
    context_object_name = 'hosting'
    paginate_by = 10

class HostingAccountDetailView(LoginRequiredMixin, DetailView):
    model = HostingAccount
    template_name = 'hosting/hosting_detail.html'
    context_object_name = 'hostin'
    
class HostingAccountCreateView(LoginRequiredMixin, CreateView):
    model = HostingAccount
    template_name = 'hosting/hosting_form.html'
    form_class = HostingAccountForm
    
    def get_success_url(self):
        return reverse_lazy('hosting:detail', kwargs={'pk': self.object.pk})

class HostingAccountUpdateView(LoginRequiredMixin, UpdateView):
    model = HostingAccount
    template_name = 'hosting/hosting_form.html'
    form_class = HostingAccountForm
    
    def get_success_url(self):
        return reverse_lazy('hosting:detail', kwargs={'pk': self.object.pk})
