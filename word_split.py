#Write a program that accepts a sequence of whitespace separated words as input
#and prints the words after removing all duplicate words and sorting them
#alphanumerically.
#Suppose the following input is supplied to the program:
#Input: hello world and practice makes perfect and hello world again
# Then, the output should be:
# Output: again and hello makes perfect practice world

#program:

word=input().split()
word_set=set(word)
print(' '.join(sorted(word_set)))
