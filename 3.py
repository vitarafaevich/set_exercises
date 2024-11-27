sw_eater = set(input('Sladkoezhkin, enter what u like: ').split())
num = int(input('how manu friend do u have?: '))
for i in range(num):
    sw_eater-=set(input(f'friend number {i} enter the food u like: ').split())
print(f'only Sladkoezhkin likes', *sw_eater)
