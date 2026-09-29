
n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

new = []

for x in a:
    if x not in new:
        new.append(x)

print("Original array:", a)
print("Unique elements:", new)
