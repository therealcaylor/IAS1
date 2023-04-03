# Write a program that reads a text file and prints the number of lines in the file to the console.

def line_counter(file_name:str):
    file = open(file_name)
    data = file.readlines()
    # readlines mthod returns an array of strings where each 
    # string represents a line.
    return len(data)

print(line_counter("test.txt"))