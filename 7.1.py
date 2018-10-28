def convert(Celsius):
    Fahrenheit = Celsius * 1.8 + 32
    return Fahrenheit


def table(x):
       for Celsius in range(-30, 50, 10):
        F = convert(Celsius)
        print (Celsius, F,  sep='      ')

print('C', 'F', sep ='         ')

print(table('Celsius'))



