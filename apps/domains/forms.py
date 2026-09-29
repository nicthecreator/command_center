from django import forms
from .models import Domain

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['domain', 'project', 'client', 'registrar', 'registration_date', 'expiration_date', 'status', 'auto_renew', 'notes']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            else:
                field.widget.attrs['class'] = 'w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
