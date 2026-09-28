# Number Hashing Using a Dictionary.
arr = [5, 2, 5, 3, 5, 2, 4, 5]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


# Number Hashing Using a Hash Array/List.
arr = [5, 2, 5, 3, 5, 2, 4, 5]

result = [0] * 21

for num in arr:
        result[num] += 1

print(result)

# Character Hashing Using a Dictionary.
s = "banana"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

# Character Hashing Using a Hash Array/List.
s = "banana"

freq = [0] * 26

for ch in s:
    index = ord(ch) - ord('a')
    freq[index] += 1

print(freq[ord('a') - ord('a')])