from django.shortcuts import render, redirect

from equation.forms import EquationParametersForm
from equation.get_solution import calculate_solution


def get_parameters_values(request):
    if request.method == 'POST':
        form = EquationParametersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return redirect('solution',
                            a=cd['parameter_a'] or 0,
                            b=cd['parameter_b'] or 0,
                            c=cd['parameter_c'] or 0)
    else:
        form = EquationParametersForm()
    return render(request, 'main_page.html', {'form': form})


def get_solution(request, a, b, c):
    solution = {}
    solution['x1'], solution['x2'] = calculate_solution(int(a),
                                                        int(b),
                                                        int(c))

    return render(request, 'solution.html', solution)