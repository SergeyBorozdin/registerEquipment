from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['photo', 'name', 'dimension1', 'dimension2', 'dimension3', 'supplier_art', 'quantity', 'storage_location']
