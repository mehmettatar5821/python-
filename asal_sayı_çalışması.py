number=int(input("enter a number: "))
prime_number=True
if(number<0):
    print("You entered a negative number, please enter a positive number")
elif(number>0 and number<2):
    print("The smallest prime number is 2.")
else:
    for i in range(2,int(number**0.5)+1):
        if(number %i == 0):
            prime_number=False
            break     
    if(prime_number):
        print(f"{number} is prime number.")
    else:
        print(f"{number} is not prime number.")