print("Enter the string whose vowel count you want:\n")
s = input()
i=0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for letter in s:
    if letter == "a":
        a_count += 1

    if letter == "e":
        e_count += 1

    if letter == "i":
        i_count += 1

    if letter == "o":
        o_count += 1

    if letter == "u":
        u_count += 1

vowel_count = a_count + e_count + i_count + o_count + u_count
print("Total vowel count is: " + str(vowel_count))
print(" 'a' count is: " + str(a_count))
print(" 'e' count is: " + str(e_count))
print(" 'i' count is: " + str(i_count))
print(" 'o' count is: " + str(o_count))
print(" 'u' count is: " + str(u_count))


