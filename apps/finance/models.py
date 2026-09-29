from django.db import models
from django.db.models import Sum
from apps.core.models import TimeStampedModel
from apps.projects.models import Project
from apps.clients.models import Client

class Sale(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        PARTIAL = 'PARTIAL', 'Parcialmente Pago'
        PAID = 'PAID', 'Pago'
        CANCELLED = 'CANCELLED', 'Cancelado'
        
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales', verbose_name='Projeto')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales', verbose_name='Cliente')
    amount = models.DecimalField('Valor Total', max_digits=10, decimal_places=2)
    sale_date = models.DateField('Data da Venda', null=True, blank=True)
    status = models.CharField('Status', max_length=20, choices=Status.choices, default=Status.PENDING)
    notes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['-sale_date']

    def __str__(self):
        return f"Venda #{self.pk} - {self.client or 'Sem cliente'}"

    @property
    def total_paid(self):
        paid = self.payments.filter(status='COMPLETED').aggregate(total=Sum('amount'))['total']
        return paid or 0

    @property
    def pending_balance(self):
        return self.amount - self.total_paid

class Payment(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        COMPLETED = 'COMPLETED', 'Concluído'
        FAILED = 'FAILED', 'Falhou'
        REFUNDED = 'REFUNDED', 'Reembolsado'

    class PaymentMethod(models.TextChoices):
        PIX = 'PIX', 'Pix'
        CREDIT_CARD = 'CREDIT_CARD', 'Cartão de Crédito'
        BANK_SLIP = 'BANK_SLIP', 'Boleto'
        TRANSFER = 'TRANSFER', 'Transferência'
        CASH = 'CASH', 'Dinheiro'
        OTHER = 'OTHER', 'Outro'

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='payments', verbose_name='Venda')
    amount = models.DecimalField('Valor do Pagamento', max_digits=10, decimal_places=2)
    payment_date = models.DateField('Data do Pagamento')
    payment_method = models.CharField('Método de Pagamento', max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.PIX)
    status = models.CharField('Status', max_length=20, choices=Status.choices, default=Status.PENDING)
    notes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-payment_date']

    def __str__(self):
        return f"Pgto #{self.pk} - {self.sale}"
