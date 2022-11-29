# shopping bill generator / calculator

sum = 0
while (True):
    userinput = input("Enter a product price or press z to quit: \n")
    if (userinput!='z'):
        sum = sum + int(userinput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Total bill amount is {sum}. Thanks for shopping with us.")
        break
