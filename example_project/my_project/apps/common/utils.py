import random

def generate_random_value(length=8):

    char_set = string.ascii_uppercase + string.digits

    char_string = ''
    # Generate the string
    for index in range(length):
        char_string += random.choice(char_set)

    return char_string

def first_letters(queryset, column_name):
    # Get list of first letters of each queryset
    letters = list()
    for row in queryset:
        try:
            char = getattr(row, column_name).upper()[0]
        except IndexError:
            char = ''
        if not char.isalpha():
            char = '#'
        if char not in letters:
            letters.append(char)

    # alphabetize them for display before returning
    letters.sort()
    return letters
