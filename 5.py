def eratos(n):
    numbers = set(range(2, n))
    for num in range(2, int(n**0.5) + 1):
        if num in numbers:
            updt = set(range(num * 2, n, num))
            numbers-=updt
    return sorted(numbers)

n = int(input('input the last number of the sequence: '))
if n > 1:
    print(f'even numbers less than {n}: {eratos(n)}')
else:
    print('please enter the number > 1')
