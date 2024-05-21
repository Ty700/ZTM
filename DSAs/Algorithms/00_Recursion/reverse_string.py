def reverse_string(string):
    if len(string) == 0:
        return ''
    else:
        return reverse_string(string[1:]) + string[0]

reversed_str = reverse_string('Tyler')
print(reversed_str)