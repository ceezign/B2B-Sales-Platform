from django import forms
from .models import ProductRequest


class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ['company_name', 'contact_person', 'email', 'phone', 'quantity', 'message']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Acme Corporation',
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'business@example.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-0000',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 500',
                'min': 1,
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes, specifications, or questions...',
                'rows': 4,
            }),
        }
        labels = {
            'company_name': 'Company Name',
            'contact_person': 'Contact Person',
            'email': 'Business Email',
            'phone': 'Phone Number',
            'quantity': 'Requested Quantity',
            'message': 'Additional Message',
        }

    def clean_quantity(self):
        qty = self.cleaned_data.get('quantity')
        if qty and qty < 1:
            raise forms.ValidationError('Quantity must be at least 1.')
        return qty
