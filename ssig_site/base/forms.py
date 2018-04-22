from django import forms
from ssig_site.base import models


class TextInput(forms.TextInput):
    template_name = 'forms/widgets/input.html'


class Textarea(forms.Textarea):
    template_name = 'forms/widgets/textarea.html'


class SplitDateTimeWidget(forms.SplitDateTimeWidget):
    template_name = 'forms/widgets/splitdatetime.html'


class NumberInput(forms.NumberInput):
    template_name = 'forms/widgets/input.html'


class Select(forms.Select):
    template_name = 'forms/widgets/select.html'


class EventForm(forms.ModelForm):

    class Meta:
        model = models.Event
        fields = '__all__'
        field_classes = {
            'start_datetime': forms.SplitDateTimeField,
            'end_datetime': forms.SplitDateTimeField,
        }
        widgets = {
            'group': forms.HiddenInput(),
            'title': TextInput(),
            'restricted_to': Select(),
            'short_description': Textarea(),
            'long_description': Textarea(),
            'start_datetime': SplitDateTimeWidget(),
            'end_datetime': SplitDateTimeWidget(),
            'location': TextInput(),
            'latitude': NumberInput(),
            'longitude': NumberInput(),
        }
