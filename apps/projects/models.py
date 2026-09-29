from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel
from apps.clients.models import Client

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug', max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug', max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(TimeStampedModel):
    class Status(models.TextChoices):
        DEVELOPMENT = 'DEVELOPMENT', 'Em Desenvolvimento'
        WAITING_CLIENT = 'WAITING_CLIENT', 'Aguardando Cliente'
        READY = 'READY', 'Pronto'
        PUBLISHED = 'PUBLISHED', 'Publicado'
        SOLD = 'SOLD', 'Vendido'
        MAINTENANCE = 'MAINTENANCE', 'Em Manutenção'
        OFFLINE = 'OFFLINE', 'Offline'
        PAUSED = 'PAUSED', 'Pausado'
        CANCELLED = 'CANCELLED', 'Cancelado'
        ARCHIVED = 'ARCHIVED', 'Arquivado'

    class PaymentStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        PARTIAL = 'PARTIAL', 'Parcial'
        PAID = 'PAID', 'Pago'

    name = models.CharField('Nome do Projeto', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True)
    description_short = models.CharField('Resumo', max_length=255, blank=True, null=True)
    description = models.TextField('Descrição', blank=True, null=True)
    
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects', verbose_name='Cliente')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects', verbose_name='Categoria')
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True, verbose_name='Tecnologias')
    
    status = models.CharField('Status', max_length=30, choices=Status.choices, default=Status.DEVELOPMENT)
    
    featured = models.BooleanField('Destaque', default=False)
    public_visible = models.BooleanField('Público', default=False)
    
    sold = models.BooleanField('Vendido', default=False)
    sale_value = models.DecimalField('Valor de Venda', max_digits=10, decimal_places=2, null=True, blank=True)
    sale_date = models.DateField('Data de Venda', null=True, blank=True)
    payment_status = models.CharField('Status de Pagamento', max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    
    completion_date = models.DateField('Data de Conclusão', null=True, blank=True)
    
    site_url = models.URLField('URL do Site', max_length=255, blank=True, null=True)
    staging_url = models.URLField('URL de Staging', max_length=255, blank=True, null=True)
    repository_url = models.URLField('URL do Repositório', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name='Projeto')
    image = models.ImageField('Imagem', upload_to='projects/images/')
    caption = models.CharField('Legenda', max_length=255, blank=True, null=True)
    is_cover = models.BooleanField('Capa', default=False)
    sort_order = models.PositiveIntegerField('Ordem', default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Imagem do Projeto'
        verbose_name_plural = 'Imagens do Projeto'
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"Imagem de {self.project.name}"
