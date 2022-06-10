
from django import forms

from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=('title','text')
        labels = dict(text='Write your thoughts')
        widgets= dict(
            title=forms.TextInput(attrs={'class':'form-control'}),
            text=forms.Textarea(attrs={'class':'form-control mb-3'})
            )

    def clean_title(self):
        title=self.cleaned_data['title']
        if 'django' not in title.lower():
            raise forms.ValidationError('We only accept notes about Django!')

        return title