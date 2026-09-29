from django.db import models
from apps.core.models import TimeStampedModel

class Client(TimeStampedModel):
    name = models.CharField('Nome', max_length=255)
    company_name = models.CharField('Razão Social / Empresa', max_length=255, blank=True, null=True)
    document = models.CharField('CPF/CNPJ', max_length=50, blank=True, null=True)
    email = models.EmailField('E-mail', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=30, blank=True, null=True)
    whatsapp = models.CharField('WhatsApp', max_length=30, blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)
    notes = models.TextField('Observações', blank=True, null=True)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

    def __str__(self):
        if self.company_name:
            return f"{self.name} ({self.company_name})"
        return self.name
