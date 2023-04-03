# Write a program that reads a CSV file and prints its contents to the console.
import csv
def csv_reader(file_name):
    file = open(file_name, "r")
    reader = csv.reader(file)
    for row in reader:
        print(row)

csv_reader("test.csv")