
n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

print("Original array:", a)

print("Reverse array:", a[::-1])
       