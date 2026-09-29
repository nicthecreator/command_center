from django.db import models
from apps.core.models import TimeStampedModel
from apps.projects.models import Project
from apps.clients.models import Client

class MaintenanceContract(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='maintenance_contracts', verbose_name='Projeto')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='maintenance_contracts', verbose_name='Cliente')
    
    active = models.BooleanField('Ativo', default=True)
    monthly_value = models.DecimalField('Valor Mensal', max_digits=10, decimal_places=2)
    
    start_date = models.DateField('Data de Início')
    next_billing_date = models.DateField('Próxima Cobrança', null=True, blank=True)
    
    description = models.CharField('Descrição/Escopo', max_length=255, blank=True, null=True)
    notes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = 'Contrato de Manutenção'
        verbose_name_plural = 'Contratos de Manutenção'
        ordering = ['next_billing_date']

    def __str__(self):
        return f"Manutenção - {self.project or self.client}"
