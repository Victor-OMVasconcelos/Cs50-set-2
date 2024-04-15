answer = input()
for letter in answer:
    if letter.lower() in ["a","e","i","o","u"]:
        answer = answer.replace(letter,"")
print(answer)