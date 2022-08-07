max = int(input("Enter a number"))
sum = 0

for i in range(1,max+1):
    if i % 2 == 0:
        sum = sum +i

print(sum)
