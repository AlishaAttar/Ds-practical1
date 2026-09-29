

n = int(input("Enter number of elements: "))

a = []
for i in range(n):
    a.append(int(input("Enter element: ")))

largest = max(a)
smallest = min(a)

a.remove(largest)
second_largest = max(a)

a.remove(smallest)
second_smallest = min(a)

print("Largest =", largest)
print("Second Largest =", second_largest)
print("Smallest =", smallest)
print("Second Smallest =", second_smallest)






