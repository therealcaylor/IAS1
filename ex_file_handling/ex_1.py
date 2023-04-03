# Write a program that reads a text file and prints its contents to the console.

def read_from_file(name_file:str):
    file = open(name_file)
    data = file.read()
    file.close()
    return data

print(read_from_file("test.txt"))