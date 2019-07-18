print("Enter string")
s = input()
char_count=0
word_count=1

for letter in s:
        char_count += 1
        if(letter==' '):
            word_count += 1


print("Word count is:" +str(word_count))