# A program to print a given string in reserve order

text = input("Please enter any string\n")
text_reverse = [letter for letter in text.split()]
print()
final = "".join(list(reversed(text_reverse[0])))
print(final)

print ("Another Method")
textLength = len(text)
while textLength > 0:
    print(text[textLength - 1],end='')
    textLength -= 1
