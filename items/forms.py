from django import forms

from core.models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border mb-3'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'location')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'location')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
