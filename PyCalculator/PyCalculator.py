operation = True
while operation:
    val = int(input("Enter a First Value\n"))
    val1 = int(input('Enter a Second Value\n'))
    op = input('Enter a operator\n')
    if op == '+':
        print(f'Sum of {val} and {val1} is: {int(val) + int(val1)}')
    elif op == '-':
        print(f'Substation of {val} and {val1} is: {val - val1}')
    elif op == '*':
        print(f'Multiplication of {val} and {val1} is: {val * val1}')
    elif op == '/':
        print(f'Division of {val} and {val1} is: {val / val1}')
    else:
        print('Invalid Operator')
        operation = False