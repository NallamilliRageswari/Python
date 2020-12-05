#Write a program that accepts a sentence and calculate the number of letters
#and digits.
#Suppose the following input is supplied to the program:

#hello world! 123
#Then, the output should be:

#LETTERS 10
#DIGITS 3



###PROGRAM:
S=input()
d=i=0
for count in S:
    if count.isdigit():
        d=d+1
    elif count.isalpha():
        i=i+1
    else:
        pass
print("LETTERS  ",i)
print("DIGITS   ",d)

