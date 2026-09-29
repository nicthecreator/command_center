from django.db import models
from django.utils import timezone
from apps.core.models import TimeStampedModel
from apps.projects.models import Project
from apps.clients.models import Client
from datetime import date

class Domain(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Ativo'
        EXPIRING = 'EXPIRING', 'Expirando'
        EXPIRED = 'EXPIRED', 'Expirado'
        CANCELLED = 'CANCELLED', 'Cancelado'
        UNKNOWN = 'UNKNOWN', 'Desconhecido'

    domain = models.CharField('Domínio', max_length=255, unique=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='domains', verbose_name='Projeto')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='domains', verbose_name='Cliente')
    
    registrar = models.CharField('Registradora', max_length=255, blank=True, null=True)
    registration_date = models.DateField('Data de Registro', null=True, blank=True)
    expiration_date = models.DateField('Data de Vencimento', null=True, blank=True)
    
    status = models.CharField('Status', max_length=20, choices=Status.choices, default=Status.ACTIVE)
    auto_renew = models.BooleanField('Renovação Automática', default=False)
    notes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = 'Domínio'
        verbose_name_plural = 'Domínios'
        ordering = ['expiration_date', 'domain']

    def __str__(self):
        return self.domain

    @property
    def days_until_expiration(self):
        if not self.expiration_date:
            return None
        hoje = timezone.now().date()
        delta = self.expiration_date - hoje
        return delta.days
