import csv

infile = open('AI.txt', 'r')

#text = csv.reader(infile, delimiter = ' ')

my_word = {}
for line in infile:
    words = line.split(" ")

    for word in words:
        if word in my_word:
            my_word[word] += 1
        else:
            my_word[word] = 1

infile.close()

print(my_word)