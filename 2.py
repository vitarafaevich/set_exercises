num = int(input('how many students are there? '))
comm = set(input('enter the first student courses: ').split())
for i in range(2, num + 1):
    comm&=set(input(f'enter the {i} student courses choice: ').split())
print(f'the number of courses everybody choose {len(comm)}')

