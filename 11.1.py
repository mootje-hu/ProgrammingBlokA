aantal = input('Met hoeveel ga je? :')

try:
    print(4356 / int(aantal))

except ZeroDivisionError:
    print('Aantal = 0 - Delen door nul kan niet!')

except ValueError:
    print('Aantal = ' +str(aantal) + '. Gebruik cijfers voor het invoeren van het aantal!')

except:
    print('Onjuiste uitvoer!')

if int(aantal) < 0:
    print('Aantal = ' +str(aantal)+'. Negatieve getallen zijn niet toegestaan!')
