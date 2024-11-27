line = set(int(i) for i in input('enter the first line of elements: ').split())
line_2 = set(int(i) for i in input('enter the second line of elements: ').split())
num = int(input('enter the number u want to check: '))
line &= line_2
if num in line:
    print('yes')
else:
    print('no')
