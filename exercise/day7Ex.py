# exercise 1

names = ["john smith","jay shanti", "eva kuki"]
print(str(names).title())
# using list comprehension
names = [name.title() for name in names]
print(names)

# exercise2
usernames = ["john 1990", "alberta1970", "mangola2000"]
usernames_char = [len(name) for name in usernames]
print(usernames_char)

# exercise3\

user_entries = ['10','19.1','20']
deci = [float(x) for x in user_entries ]
print(deci)

# EXERCISE 4

user_entries = ['10','19.1','20']
deci = [float(x) for x in user_entries ]
# add = [sum(x) for x in user_entries]
# print(add)
add = sum(deci)
print(add)
