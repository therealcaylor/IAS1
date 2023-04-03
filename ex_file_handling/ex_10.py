# 10- Write a program that reads a binary file and converts it's content to ASCII string


file = open("./ex_file_handling/ex_10.txt", "rb")
data = file.read()
# remove the '0b' prefix from the binary string
binary_string = data[2:].decode('utf-8')
# convert each 8-bit substring to its corresponding ASCII character
output_string = ''.join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])

print(output_string)