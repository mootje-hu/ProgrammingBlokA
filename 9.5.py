def namen():
    names = {}
    while True:
        name_in = input('Volgende naam: ')
        if len(name_in) == 0:
            for name, count in names.items():
                if count == 1:
                    print('Er is ' + str(count) + ' student met de naam ' + name)
                elif count > 1:
                    print('Er zijn ' + str(count) + ' studenten met de naam' + name)
            break
        else:
            names_exist = names.keys()
            if name_in in names_exist:
                names[name_in] += 1
            else:
                names[name_in] = 1
namen()