# Naam: Karoen Indraj
# Studentnummer: 1821689
# Project Zuil

import datetime
import random

def bericht():
    tekst = input("Uw bericht: ")
    return tekst

def reiziger():
    naam = input("Voer uw naam in: ")
    if len(naam) > 0 and naam.strip():
        return naam
    else:
        naam = "Anoniem"
        return naam

def datum_tijd():
        localtime = datetime.datetime.now()
        tijd = localtime.strftime("%d-%m-%Y %H:%M:%S")
        return tijd

def stations():
    lst = ("Utrecht","Amsterdam","Den Haag")
    item = random.choice(lst)
    return item

def save_data():
    file = open("myfile.txt", "a")
    file = file.write(str(reiziger())),file.write(","),file.write(str(bericht())),file.write(","),\
           file.write(str(datum_tijd())),file.write(","),file.write(stations()),file.write("\n")
    return file
    file.close()

print(save_data())