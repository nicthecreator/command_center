from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client', 'category', 'technologies', 'status', 'description', 'site_url']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxSelectMultiple) or isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 w-full'
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            else:
                field.widget.attrs['class'] = 'w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
