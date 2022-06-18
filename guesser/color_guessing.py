import random
from django.conf import settings
from django import forms


def remove_subject_from_list(subject_number):
    if subject_number in settings.SUBJECT_NUMBERS:
        settings.SUBJECT_NUMBERS.remove(subject_number)


def guess_color(subject_number):
    remove_subject_from_list(subject_number)

    color = random.choices(['синий', 'зеленый', 'красный'],
                           weights=settings.BLUE_GREEN_RED_WEIGHTS)
    if color == ['синий']:
        settings.BLUE_GREEN_RED_WEIGHTS[0] -= 1
    if color == ['зеленый']:
        settings.BLUE_GREEN_RED_WEIGHTS[1] -= 1
    if color == ['красный']:
        settings.BLUE_GREEN_RED_WEIGHTS[2] -= 1

    return color[0]
