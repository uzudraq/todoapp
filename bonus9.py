password = input("Enter a mew password: ")
result = {}

if len(password) >= 8:
    result["Length"] = (True)
else:
    result['Length']=(False)

digit = False
for char in password:
    if char.isdigit():
        digit = True

result["digits"]= digit

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
result["uppercasee"] = uppercase

print(result)
print(result.values())
print(type(result))
if all(result.values()):
    print("Password is strong")
else:
    print("Password is weak")