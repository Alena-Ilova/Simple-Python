a = int(input('3890'))
b = int(input('489'))
c = int(input('2939'))
if a>b:
    a, b = b, a
if a>c:
    a, c = c, a
if b>c:
    b, c = c, b
print(f'Sorted integres: ({a}, {b}, {c})')