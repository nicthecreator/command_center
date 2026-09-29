from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum, Count
from django.utils import timezone
from apps.projects.models import Project
from apps.domains.models import Domain
from apps.hosting.models import HostingAccount
from apps.finance.models import Sale
from apps.maintenance.models import MaintenanceContract

@login_required
def dashboard_view(request):
    # 1. Total de Projetos Ativos (Em Desenvolvimento ou Pronto)
    active_projects = Project.objects.filter(status__in=['DEVELOPMENT', 'READY'])
    active_projects_count = active_projects.count()

    # 2. MRR (Receita Recorrente Mensal)
    mrr_aggregate = MaintenanceContract.objects.filter(active=True).aggregate(total=Sum('monthly_value'))
    mrr = mrr_aggregate['total'] or 0

    # 3. Valores Pendentes (A Receber)
    sales = Sale.objects.exclude(status='CANCELLED')
    pending_receivables = sum(sale.pending_balance for sale in sales if sale.pending_balance > 0)

    # 4. Próximos Vencimentos (Domínios e Hospedagens)
    upcoming_domains = Domain.objects.filter(
        status='ACTIVE', 
        expiration_date__gte=timezone.now().date()
    ).order_by('expiration_date')[:5]

    upcoming_hosting = HostingAccount.objects.filter(
        status='ACTIVE',
        expiration_date__gte=timezone.now().date()
    ).order_by('expiration_date')[:5]

    # Dados para o Gráfico (Projetos por Status)
    project_status_counts = Project.objects.values('status').annotate(count=Count('id'))
    status_labels = []
    status_data = []
    status_dict = dict(Project.Status.choices)
    for p in project_status_counts:
        status_labels.append(status_dict.get(p['status'], p['status']))
        status_data.append(p['count'])

    context = {
        'active_projects_count': active_projects_count,
        'mrr': mrr,
        'pending_receivables': pending_receivables,
        'upcoming_domains': upcoming_domains,
        'upcoming_hosting': upcoming_hosting,
        'chart_labels': status_labels,
        'chart_data': status_data,
    }

    return render(request, 'dashboard/dashboard.html', context)

@login_required
def analytics_view(request):
    return render(request, 'dashboard/analytics.html')

@login_required
def monitoring_view(request):
    projects_with_urls = Project.objects.exclude(site_url='').exclude(site_url__isnull=True)
    context = {'projects': projects_with_urls}
    return render(request, 'dashboard/monitoring.html', context)

@login_required
def alerts_view(request):
    # Domínios vencendo em 30 dias ou vencidos
    from datetime import timedelta
    limit_date = timezone.now().date() + timedelta(days=30)
    
    domains_alert = Domain.objects.filter(status='ACTIVE', expiration_date__lte=limit_date).order_by('expiration_date')
    hosting_alert = HostingAccount.objects.filter(status='ACTIVE', expiration_date__lte=limit_date).order_by('expiration_date')
    
    # Pagamentos atrasados (pendentes e data no passado)
    from apps.finance.models import Payment
    late_payments = Payment.objects.filter(status='PENDING', payment_date__lt=timezone.now().date()).order_by('payment_date')
    
    context = {
        'domains_alert': domains_alert,
        'hosting_alert': hosting_alert,
        'late_payments': late_payments
    }
    return render(request, 'dashboard/alerts.html', context)


from .forms import UserSettingsForm
from django.contrib import messages

@login_required
def settings_view(request):
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Suas configurações foram atualizadas com sucesso!')
    else:
        form = UserSettingsForm(instance=request.user)
        
    return render(request, 'dashboard/settings.html', {'form': form})

