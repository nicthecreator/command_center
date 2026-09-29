from django.contrib import admin
from .models import Category, Technology, Project, ProjectImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'status', 'category', 'public_visible', 'sold', 'created_at')
    list_filter = ('status', 'public_visible', 'sold', 'category')
    search_fields = ('name', 'description', 'client__name', 'client__company_name')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('client', 'technologies', 'category')
    inlines = [ProjectImageInline]
    
    fieldsets = (
        ('Informações Principais', {
            'fields': ('name', 'slug', 'client', 'category', 'technologies')
        }),
        ('Descrição', {
            'fields': ('description_short', 'description')
        }),
        ('Status e Visibilidade', {
            'fields': ('status', 'featured', 'public_visible')
        }),
        ('Informações Comerciais', {
            'fields': ('sold', 'sale_value', 'sale_date', 'payment_status', 'completion_date')
        }),
        ('URLs', {
            'fields': ('site_url', 'staging_url', 'repository_url')
        }),
    )
