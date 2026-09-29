n=int(input("Enter number of elements"))
a=[]
for i in range(n):
    a.append(int(input("Enter the elements")))
even=0
odd=0
for x in a:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of Even elements =", even)
print("Number of Odd elements =", odd)