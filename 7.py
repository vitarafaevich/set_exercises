from itertools import permutations

def lexico(numbers):
    num = sorted(numbers)
    per = permutations(num)
    for i in per:
        print(i)

nums = set(int(i) for i in input('enter some numbers: ').split())
lexico(nums)