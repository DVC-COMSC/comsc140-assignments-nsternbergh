#print numbers in ascending order
number1_ = int(input("Enter number1_"))
number2_ = int(input("Enter number2_"))
number3_ = int(input("Enter number3_"))
if (int(number1_)) < (int(number2_)) < (int(number3_)):
  print (number1_ , number2_ , number3_)
if (int(number3_)) < (int(number2_)) < (int(number1_)):
  print (number3_ , number2_, number1_)
elif (int(number2_)) < (int(number1_)) < (int(number3_)):
  print (number2_, number1_ , number3_)
elif (int(number2_)) < (int(number3_)) < (int(number1_)):
  print (number2_ , number3_ , number1_)