print("Enter the English word you want to alter")
word = input()

first_letter = word[0]
remaining_letters = word[1:]
affixer = "ay"

pig_latin = remaining_letters + first_letter + affixer
print(pig_latin)