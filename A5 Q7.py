# Python Code to check if a number is
# Positive, Negative, Odd, Even, Zero
# Using if...elif...else
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
 
# Checking for odd and even
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
