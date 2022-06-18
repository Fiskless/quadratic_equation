from django import forms
from django.conf import settings


class SubjectNumberForm(forms.Form):
    number = forms.IntegerField(label='Номер предмета от 1 до 100:')

    def clean_number(self):
        number = self.cleaned_data['number']
        if 1 > number or number > 100:
            raise forms.ValidationError('Номер должен быть от 1 до 100')
        if number not in settings.SUBJECT_NUMBERS:
            raise forms.ValidationError('Предмета с таким номером нет')
        return number
