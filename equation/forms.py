from django import forms


class EquationParametersForm(forms.Form):
    parameter_a = forms.IntegerField(label='Введите коэффициент a', required=False)
    parameter_b = forms.IntegerField(label='Введите коэффициент b')
    parameter_c = forms.IntegerField(label='Введите коэффициент c')