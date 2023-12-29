import csv
with open("tested.csv", 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    countAdult = 0
    countChildren = 0
    countAdultAlive = 0
    countChildrenAlive = 0
    countAllPassangers = 0
    countAgeIndex = 0
    countSurvivedIndex = 0

    for row in my_reader:
        if countAllPassangers == 0:
            for item in row:
                if item == 'Age' or item == 'Возраст':
                    ageIndex= countAgeIndex
                else: countAgeIndex +=1
                if item == 'Survived' or item == 'Выжил':
                    survivedIndex = countSurvivedIndex
                else: countSurvivedIndex +=1

        print(row)
        if countAllPassangers > 0 :
            if row[ageIndex] != '':
                if float(row[ageIndex]) >= 18 :
                    countAdult +=1
                    if row[survivedIndex] == '1':
                        countAdultAlive +=1
                elif float(row[ageIndex]) < 18:
                    countChildren+=1
                    if row[survivedIndex]== '1':
                        countChildrenAlive +=1
                else :
                    break
        countAllPassangers +=1
    print(f" Всего людей было = {countAllPassangers}, Всего взрослых = {countAdult}, Всего детей = {countChildren}, Выживших взрослых = {countAdultAlive},"
          f"Выживших детей = {countChildrenAlive}")
