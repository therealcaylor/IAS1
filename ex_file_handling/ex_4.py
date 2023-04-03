# Write a program that reads a text file and prints the number of characters in the file to the console.


def character_counter(file_name:str):
    counter = 0
    file = open(file_name)
    data = file.read()
    for i in data:
        counter +=1
    return counter

character_counter("test.txt")