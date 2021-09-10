

try:
    result = None
    a = float(input('Number 1: '))
    b = float(input('Number 2: '))
    result = a/b
except ZeroDivisionError as e:  # error class specified
    print('exception is ', type(e))
except ValueError as e:
    print('add only values unless ', type(e))
else:
    print('mistake in giving input')

print('Result = ', result)
print('End')    # at exception; this will also not run.
