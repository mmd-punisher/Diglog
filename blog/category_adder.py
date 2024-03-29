from .models import Category


def display_choices():
    choices = Category.objects.all().values_list('name', 'name')
    choices_list = []
    for choice in choices:
        choices_list.append(choice)

    return choices_list
