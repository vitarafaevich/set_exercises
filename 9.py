from itertools import combinations

def subsets(nums, k):
    k_elmnt = set(combinations(nums, k))
    print(k_elmnt)

numbers = set(int(i) for i in input('enter some numbers: ').split())
kk = int(input('enter the subset lenght: '))
subsets(numbers, kk)