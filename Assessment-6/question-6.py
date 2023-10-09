tups = [("1", "4"), ("4", "1"), ("3", "4"), ("2", "7"), ("6", "8"), ("5", "8"), ("6", "8"), ("5", "7"), ("2", "7")]
freq = {}

for i in range(len(tups)):
    tups[i] = sorted(tups[i])
    out = f"('{tups[i][0]}', '{tups[i][1]}')"
    tups[i] = out

for tup in tups:
    if tup in freq:
        freq[tup] += 1
    else:
        freq[tup] = 1

print("Tuples frequency")
for tup in freq:
    print(f"{tup} {freq[tup]}")