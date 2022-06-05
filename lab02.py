


num = int(input("Input an integer (0 terminates): \n"))
oddSum  = 0
evenSum = 0
oddCount = 0 
evenCount = 0 
positiveIntCount = 0


while(num != 0):
    if(num < 0):
        print("You entered a negative number. Negative numbers are not allowed\n")
    elif(num > 0):
        positiveIntCount += 1
        if(num % 2 == 0):
            evenCount += 1
            evenSum = evenSum + num
        else:
            oddCount += 1
            oddSum = oddSum + num
    num = int(input("Input an integer (0 terminates): \n"))
        


print()
print("sum of odds:", oddSum)
print("sum of evens:", evenSum)
print("odd count:", oddCount)
print("even count:", evenCount)
print("total positive int count:", positiveIntCount)