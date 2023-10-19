no_of_rotation = int(input("Enter the number of times you want to rotate the list : ")).__abs__()

print("Original deque:")
deque = ["Venus", "Earth", "Mars", "Jupiter"]
print(deque)

for i in range(1, no_of_rotation + 1):
    for j in range(i):
        deque.insert(0, deque.pop())
    print(f"\nDeque after {i} positive rotation")
    print(f"deque({deque})")