import random
import csv

class Chance:
    __massages = []
    __moneys = []
    def choice(self):
        with open('chance.csv','r',encoding ='utf-8') as csvfile :
            rows = csv.DictReader(csvfile)
            for row in rows :
                self.__massages.append(row['機會'])
                self.__moneys.append(row['金額'])
        index = random.randrange(0,len(self.__massages))
        return ([self.__massages[index],self.__moneys[index]])

if __name__ == "__main__":
    myChance = Chance()
    print(myChance.choice())