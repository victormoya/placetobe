from django import forms
from bootstrap3_datetime.widgets import DateTimePicker


from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('assistants', 'publisher', 'confirmed')
        fields = ['title', 'description', 'location', 'date', 'category', 'image', 'website']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            'location': forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Street Number City Country'}),
            'date': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'http://'}),
            'category': forms.Select(attrs={'class': 'form-control', 'value': 'General'}),
        }

    def save(self, user, commit=True):
        event = super(EventForm, self).save(commit=False)
        event.publisher = user
        if commit:
            event.save()
        return event

