from django import forms

from .models import Item

CATEGORY_CHOICES = (
    ("Personal", "Personal"),
    ("Work", "Work"),
    ("Study", "Study"),
    ("Groceries", "Groceries"),
    ("Pets", "Pets"),
)


class NewItemForm(forms.ModelForm):
    """Form for adding new Task Items."""
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Sort by: ")

    term = forms.TextInput()
    description = forms.TextInput()
    finish_by = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M:%S'],
        widget=forms.DateTimeInput(format="%d/%m/%Y %H:%M:%S"),
        label='Finish by (DD/MM/YYYY HH:MM:SS)'
    )
    is_completed = forms.BooleanField(required=False)

    class Meta:
        model = Item
        fields = ('category', 'term', 'description', 'finish_by', 'is_completed', )


class CategoryForm(forms.Form):
    """Form for filtering the main page by category."""
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        fields = ('category', )
