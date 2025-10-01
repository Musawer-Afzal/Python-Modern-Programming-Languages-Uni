def greater_less(x, y):
    if x == y:
     print("Both Intergers are equal")
    elif x > y:
       print(f"{x} is greater than {y}")
    else:
       print(f"{y} is greater than {x}")

Flag = True
while Flag:
    input_1 = int(input("Enter a Number: "))
    input_2 = int(input("Enter a Number: "))
    greater_less(input_1, input_2)
    
    ask = input("Do you want to check again - y/n? ")
    if ask == "y" or ask == "yes" or ask == "Yes"  or ask == "Y":
       continue
    else:
       print("Program Terminated")
       Flag = False