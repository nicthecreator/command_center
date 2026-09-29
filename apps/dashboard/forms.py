from django import forms
from django.contrib.auth.models import User

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
