#Convertion of Hexadecimal number to Decimal number.
n = input("Enter A Hexa Decimal Number :")
dec = 0
bit = 0
for i in n[::-1]:
	try:
		r =  int(i)
	except:
		r = ord(i)-55
	dec += r*(16**bit)
	bit += 1
print("Decimal Value :",dec)
