def print_Kaprekar_nums(start, end):  
   for i in range(start, end ):  
      sqr = i ** 2  
      digits = str(sqr)  
  
      length = len(digits)  
      for x in range(1, length):  
         left = int("".join(digits[:x]))  
         right = int("".join(digits[x:]))  
         if (left + right) == i:
            print("%s "%(str(i)), end = " ")
a=int(input("Enter 1st number: "))
b=int(input("Enter 2st number: "))
print("kaprekar numbers in between "+str(a)+" and "+str(b)+ ":")
print_Kaprekar_nums(a,b)  
