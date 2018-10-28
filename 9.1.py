getallen = []
while True:
     getal = int(input('Geef een getal:'))
     if int(getal) == 0:
         break
     getallen.append(getal)
print(getallen)
print('Er zijn ' + str(len(getallen)) + ' getallen ingevoerd, de som is: ' + str(sum(getallen)))