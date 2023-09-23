from django import forms

from .models import Category, Item

INPUT_CLASSES = 'w-full px-3 py-2 border rounded shadow-inner'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image')
        
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
                }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
                }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
                }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image', 'is_reserved')
        
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
                }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
                }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
                }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'is_reserved': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
                }),
        }