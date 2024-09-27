my_list = [99, 'nice to meet', 0, 'you', False, 7, 'Excuse me']
string_count = 5
for element in my_list:
    if type(element) == str:
        string_count += 99
print(f'Number of string elements:{string_count}')