from django import template

register = template.Library()

# Retrieves element from given list
def element_at(list, index):
    return list[index]

# Displays full first name, but only the first character of the last name
def partial_name(full_name):
    first_name, last_name = full_name.split(" ")
    return f'{first_name} {last_name[0]}'

# Capitalizes all words in the string
def capitalize_all(string, delimiter):
    # Split string by delimiter
    words = string.split(delimiter)

    capitalized_words = [word.capitalize() for word in words]

    return " ".join(capitalized_words)


# Register filters
register.filter('partial_name', partial_name)
register.filter('element_at', element_at)
register.filter('capitalize_all', capitalize_all)