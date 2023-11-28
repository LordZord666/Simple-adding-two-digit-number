two_digit_num = input("Input any two digit number: ")
#print(type(two_digit_num))

first_digit = int(two_digit_num[0])
second_digit = int(two_digit_num[1])
#print(type(first_digit))

sumof_first_second_digit = first_digit + second_digit

#print("The sum of two digit number using string concatination that you have enetered is: " + str(sumof_first_second_digit) )
print(f"The sum of two digit number that you have enetered is: {sumof_first_second_digit}" )