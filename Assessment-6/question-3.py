no_of_roation = int(input("Enter the number of times you want to rotate the list : ")).__abs__()

print("Original deque:")
deque = ["Venus", "Earth", "Mars", "Jupiter"]
print(deque)

for i in range(1, no_of_roation + 1):
    for j in range(i):
        deque.append(deque.pop(0))
    print(f"\nDeque after {i} negative rotation")
    print(f"deque({deque})")