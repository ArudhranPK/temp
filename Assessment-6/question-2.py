no_of_roation = int(input("Enter the number of times you want to rotate the list : ")).__abs__()

print("Original deque:")
deque = ["Venus", "Earth", "Mars", "Jupiter"]
print(deque)

for i in range(no_of_roation):
    deque.insert(0, deque.pop())
    print(f"\nDeque after {i + 1} positive rotation")
    print(f"deque({deque})")