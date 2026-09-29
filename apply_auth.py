import os

files_to_modify = [
    'apps/projects/views.py',
    'apps/clients/views.py',
    'apps/domains/views.py',
    'apps/hosting/views.py',
    'apps/finance/views.py',
    'apps/maintenance/views.py',
]

for filepath in files_to_modify:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'LoginRequiredMixin' not in content:
        # Import
        content = "from django.contrib.auth.mixins import LoginRequiredMixin\n" + content
        
        # Replace
        content = content.replace('(ListView)', '(LoginRequiredMixin, ListView)')
        content = content.replace('(DetailView)', '(LoginRequiredMixin, DetailView)')
        content = content.replace('(CreateView)', '(LoginRequiredMixin, CreateView)')
        content = content.replace('(UpdateView)', '(LoginRequiredMixin, UpdateView)')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# Fix dashboard view
dashboard_file = 'apps/dashboard/views.py'
with open(dashboard_file, 'r', encoding='utf-8') as f:
    dash_content = f.read()

if 'login_required' not in dash_content:
    dash_content = "from django.contrib.auth.decorators import login_required\n" + dash_content
    dash_content = dash_content.replace('def dashboard_view(request):', '@login_required\ndef dashboard_view(request):')
    
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        f.write(dash_content)

print("Auth applied to all views.")
