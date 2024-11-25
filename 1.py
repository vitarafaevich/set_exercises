line = set(int(i) for i in input().split())
num = int(input())
if num in line:
    print('number', num, 'is in numbers')
else:
    print('number', num, 'is not in numbers')
