afstandKM = int(input('Hoeveel km rijdt je?:'))


def standaardprijs(afstandKM):
    if afstandKM >= 50:
        kosten = (15 + (afstandKM - 50)*0.60)
        return(kosten)
    elif afstandKM < 0:
        kosten = ('0')
        return(kosten)
    else:
        kosten = (afstandKM * 0.80)
        return(kosten)

weekendrit = input('Is het weekend?:')
leeftijd = int(input('Hoe oud ben je?'))


def ritprijs(leeftijd, weekendrit, afstandKM):
    kosten = (standaardprijs(afstandKM))
    if leeftijd >= 65 or leeftijd <= 12 and weekendrit == 'nee':
        print(float(kosten) * 0.7)
    elif leeftijd >= 65 or leeftijd <= 12 and weekendrit == 'ja':
        print(float(kosten) * 0.65)
    elif leeftijd <= 65 or leeftijd >= 12 and weekendrit == 'ja':
        print(float(kosten) * 0.6)
    else:
        print(float(kosten))

print(ritprijs(leeftijd, weekendrit, afstandKM))
