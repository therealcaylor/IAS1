# Write a program that reads a CSV file and creates a dictionary where the keys are the first column of the CSV file, and the values are the second column.

import csv

def dict_factory(file_name:str):
    file = open(file_name, "r")
    reader = csv.reader(file)
    dizionario = dict()
    for row in reader:
        dizionario[row[0]] = row[1:]
        
    return dizionario

print(dict_factory("ex_7.csv"))
