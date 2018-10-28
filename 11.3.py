import csv

with open('spelers.csv', 'r', newline='\n') as ReadCSVFile:
    top = {
        'name': '',
        'date': '',
        'score': 0
    }
    reader = csv.DictReader(ReadCSVFile, delimiter=';')

    for row in reader:
        if int(row['score']) > top['score']:
            top['name'] = row['name']
            top['date'] = row['date']
            top['score'] = int(row['score'])
print('De hoogste score is:', top['score'], 'op', top['date'], 'behaald door', top['name'])