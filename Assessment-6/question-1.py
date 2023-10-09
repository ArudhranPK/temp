deque = ["Venus", "Earth", "Mars", "Jupiter"]
print(f"deque({deque})\n")

print("Appending to the left")
deque.insert(0, "Mercury")
print(f"deque({deque})\n")

print("Appending to the right")
deque.append("Saturn")
print(f"deque({deque})\n")

print("Removing from the right")
del deque[-1]
print(f"deque({deque})\n")

print("Removing from the left")
del deque[0]
print(f"deque({deque})\n")

print("Reversing the deque")
deque = deque[::-1]
print(f"deque({deque})")