from django.conf import settings
from django.shortcuts import render, redirect

from guesser.color_guessing import guess_color
from guesser.forms import SubjectNumberForm


def get_subject_number(request):
    if request.method == 'POST':
        if 'guessing' in request.POST:
            form = SubjectNumberForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                return redirect('intended_color',
                                number=cd['number'])
        elif 'restart' in request.POST:
            form = SubjectNumberForm(request.POST)
            settings.SUBJECT_NUMBERS = [number for number in range(1, 101)]
            settings.BLUE_GREEN_RED_WEIGHTS = [60, 21, 19]
            return render(request, 'guesser_main.html', {'form': form})
    else:
        form = SubjectNumberForm(initial={'number': 1})
    return render(request, 'guesser_main.html', {'form': form})


def intend_color(request, number):
    color = guess_color(number)
    return render(request, 'intended_color.html', {'color': color})