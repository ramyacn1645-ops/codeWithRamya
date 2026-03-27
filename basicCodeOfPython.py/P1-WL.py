# to add first N natural numbers using while loop

n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    sum = sum +i
print(f"The sum of first {n} natural number is: ")
print(sum)