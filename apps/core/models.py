from django.db import models

class TimeStampedModel(models.Model):
    """
    Classe base abstrata que provê campos de
    criação (created_at) e atualização (updated_at).
    """
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True
