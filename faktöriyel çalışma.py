 #girilen sayının faktöriyelini hesaplayan program

result=1
i=1
number=int(input("enter an integer:"))
while(i<=number):
    result*=i
    i+=1
print(f"{number}!={result}")
