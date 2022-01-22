vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel"

found = set()
for i in message:
    if i in vowels:
        found.add(i)

print(found)

found2 = {i for i in message if i in vowels}
print(found2)
