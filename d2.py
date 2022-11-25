#ucitava i pretvara string sa opsegom godina u dva cela broja
def years():
    age_range = input()
    return [int(x) for x in age_range.split('-')]

#ucitava ime datoteke i podatke iz datoteke u listu ljudi i pretvara datum rodjenja u godine
def readFile():
    file_name = input()
    people = []
    with open(file_name, 'r') as file:
        next(file)
        for line in file:
            name, surname, gender, born, education = [x.strip() for x in line.strip().split(',')]
            day, month, year = [int(x) for x in born.split('/')]
            age = 2021 - year
            if month > 1 or (month == 1 and day > 1):
                age -= 1
            person = [name, surname, gender, age, education]
            people.append(person)
    return people

#filtrira listu po godinama, vraca listu sa onim ljudima cije su godine u opsegu
def yearFilter(people, age1, age2):
    return [x for x in people if x[3] >= age1 and x[3] <= age2]

#pravi listu koja treba da se upise u datoteku
def statList(people):
    num = len(people)
    stat = [['Primary', 0, 0, '|', 0, 0, '|', 0, 0],
            ['Secondary', 0, 0, '|', 0, 0, '|', 0, 0],
            ['Bachelor', 0, 0, '|', 0, 0, '|', 0, 0],
            ['Master', 0, 0, '|', 0, 0, '|', 0, 0],
            ['PHD', 0, 0, '|', 0, 0, '|', 0, 0]]
    for line in people:
        for i in range(len(stat)):
            if line[4] == stat[i][0] and line[2] == 'F':
                stat[i][1] += 1
            elif line[4] == stat[i][0] and line[2] == 'M':
                stat[i][2] += 1
    for x in stat:
        x[7] = x[1] + x[2]
        x[8] = x[7] / num * 100
        if x[7]:
            x[4] = x[1] / x[7] * 100
            x[5] = x[2] / x[7] * 100
    return stat

#unos podataka iz liste u novu datoteku "stats.txt"
def statFile(stat):
    with open('stats.txt', 'w+') as file:
        for line in stat:
            for i in range(4):
                file.write('{} '.format(line[i]))
            file.write('{:0.2f} '.format(line[4]))
            file.write('{:0.2f} '.format(line[5]))
            file.write('{} '.format(line[6]))
            file.write('{} '.format(line[7]))
            if line != stat[len(stat)-1]:
                file.write('{:0.2f}\n'.format(line[8]))
            else:
                file.write('{:0.2f}'.format(line[8]))

#glavni program
try:
    people = readFile()
    age1, age2 = years()
    filtrated = yearFilter(people, age1, age2)
    stat = statList(filtrated)
    statFile(stat)
except ValueError:
    print('GRESKA', end='')
except ZeroDivisionError:
    print('GRESKA', end='')
except FileNotFoundError:
    print('DAT_GRESKA', end='')