n=int(input("Enter number of elements"))
a=[]
for i in range(n):
    a.append(int(input("Enter the elements")))
num=int(input("Enter number to search:"))    
found = False

for i in range(n):
    if a[i] == num:
        print("Number is present at position", i + 1)
        found = True
        break
    found = False
if found== False:
    print("Element is not present")
