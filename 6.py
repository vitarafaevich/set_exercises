for i in range(108, 334):
    sum = set(str(i))
    res = set(str(i * 3))
    if len(sum|res) == len(sum) + len(res):
        print(f'{i}+{i}+{i}={i * 3}')