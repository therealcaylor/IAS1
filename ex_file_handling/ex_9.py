# Write a program that reads a binary file and prints its contents to the console.

# import binascii

with open('./ex_file_handling/ex_9.txt', 'rb') as f:
    file_contents = f.read()
# data  =binascii.unhexlify(file_contents)
data = bytes.fromhex(file_contents.decode('utf-8'))
print(data)
    