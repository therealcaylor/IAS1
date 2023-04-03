# Write a program that reads a text file and prints the number of words in the file to the console.

def word_counter(file_name:str):
    file = open(file_name)
    lines = file.readlines()
    temp = []
    for line in lines:
        splited = line.split()
        for word in splited:
            temp.append(word)
    return len(temp)

print(word_counter("test.txt"))