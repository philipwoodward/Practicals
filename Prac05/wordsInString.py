"""Counts the number of times each word appears in a string
"""

# my_string = input("Please type in a long string so I can count the number of times each word appears > ")
import operator

my_string = "this is my list of repeated words that is my dictionary of these words"
my_list = my_string.split()
my_sorted_list = []
print(my_list)
words_dict = {}
for word in my_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
print(words_dict, end=" ")
for (key, value) in words_dict.items():
    sorted(words_dict)
    print(key, value)
# for w in sorted(words_dict(items(),key=lambda x: x[1])):
#    print (w, words_dict[w])
