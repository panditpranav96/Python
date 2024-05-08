num_1=int(input("Enter First number "))
num_2=int (input("Enter Second Number ")) 

choice = input("Enter the operation + - * / ")

if choice == "+":

  sum= num_1 + num_2

  print ("The Sum of two number is",sum)

elif choice == "-":
  
    diff = num_1 - num_2
    print ("The Difference between to number is", diff)

elif choice == "/":
   
    div= num_1 / num_2
    print ("The Division between to number is", div)

elif (choice == "*"):
   
    mul= num_1 * num_2
    print ("The Multiplication between to number is", mul)
else:
    print ("Invalid Operation")