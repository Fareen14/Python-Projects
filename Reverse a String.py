def reverse(string1):
    string1 = "".join(reversed(string1))
    return string1

s = "The weather is enjoyable today!"

print("The original string is:\n ", end=" ")
print(s)

print("\nThe reversed string(using reversed function) is:\n")
print(reverse(s))

