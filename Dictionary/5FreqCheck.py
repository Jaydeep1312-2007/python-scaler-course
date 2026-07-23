name = input("Enter a Name: ")

freq = {}

for i in name:

    if i not in freq:
        freq[i] = 1

    else:
        freq[i] += 1

print(freq)