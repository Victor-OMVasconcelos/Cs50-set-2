camaelCase = input("camaelCase: ")
print("snake_case: ", end="")

for letter in camaelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

print()
   

