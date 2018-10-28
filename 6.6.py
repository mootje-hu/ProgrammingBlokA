list = ['a', 'b', 'c']

def wijzig(list):
    list.remove('a')
    list.remove('b')
    list.remove('c')
    list.append('d')
    list.append('e')
    list.append('f')
    return list

print(wijzig(list))