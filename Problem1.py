def count_char(string):
    c = 0
    for char in string:
        c += 1
    return c


int_string = "My first task"
char_count = count_char(int_string)
print(f"The number of characters in '{int_string}' is: {char_count}")