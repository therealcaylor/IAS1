# Write a program that reads a CSV file and creates a new file with the same contents, but with all the data sorted alphabetically by the first column.

import csv


def data_get(file_name:str):
    dizionario = dict()
    file = open(file_name, "r")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        dizionario[row[0]] = row[1:]
    keys = sorted(dizionario.keys())
    new_file = open("newFile.csv", "w")
    csv_writer = csv.writer(new_file)
    for key in keys:
        row = []
        row.append(key)
        content = dizionario[key]
        for c in content:
            row.append(c)
        csv_writer.writerow(row)
    return

data_get("ex_8.csv")