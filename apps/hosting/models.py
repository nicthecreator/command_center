from django.db import models
from django.utils import timezone
from apps.core.models import TimeStampedModel
from apps.projects.models import Project
from apps.clients.models import Client

class HostingAccount(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Ativa'
        SUSPENDED = 'SUSPENDED', 'Suspensa'
        CANCELLED = 'CANCELLED', 'Cancelada'

    class BillingCycle(models.TextChoices):
        MONTHLY = 'MONTHLY', 'Mensal'
        QUARTERLY = 'QUARTERLY', 'Trimestral'
        SEMI_ANNUALLY = 'SEMI_ANNUALLY', 'Semestral'
        ANNUALLY = 'ANNUALLY', 'Anual'
        BIENNIALLY = 'BIENNIALLY', 'Bienal'
        TRIENNIALLY = 'TRIENNIALLY', 'Trianual'

    provider = models.CharField('Provedor', max_length=255)
    plan = models.CharField('Plano', max_length=255, blank=True, null=True)
    server = models.CharField('Servidor (IP/Hostname)', max_length=255, blank=True, null=True)
    
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='hosting_accounts', verbose_name='Projeto')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='hosting_accounts', verbose_name='Cliente')
    
    monthly_cost = models.DecimalField('Custo Mensal Equivalente', max_digits=10, decimal_places=2, null=True, blank=True)
    billing_cycle = models.CharField('Ciclo de Faturamento', max_length=20, choices=BillingCycle.choices, default=BillingCycle.ANNUALLY)
    
    start_date = models.DateField('Data de Início', null=True, blank=True)
    expiration_date = models.DateField('Data de Vencimento', null=True, blank=True)
    
    status = models.CharField('Status', max_length=20, choices=Status.choices, default=Status.ACTIVE)
    notes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = 'Conta de Hospedagem'
        verbose_name_plural = 'Contas de Hospedagem'
        ordering = ['expiration_date', 'provider']

    def __str__(self):
        return f"{self.provider} - {self.plan or 'Plano Genérico'} ({self.project or self.client})"
    
    @property
    def days_until_expiration(self):
        if not self.expiration_date:
            return None
        hoje = timezone.now().date()
        delta = self.expiration_date - hoje
        return delta.days
