"""Forms of the project."""

# Create your forms here.
from django import forms
from form.models import Thing

class SignUpForm(froms.modelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description' : forms.Textarea(), 'quantity' : forms.NumberInput()}
