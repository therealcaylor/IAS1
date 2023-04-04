# Write a comprehension that produces a list of integers representing the lengths of the words in a given list.


word_list = ["Piquant","Luminous","Ethereal","Quixotic","Mellifluous","Ephemeral","Serendipity","Halcyon","Ineffable","Enigmatic"]

integer_list = [len(x) for x in word_list]
print(integer_list)