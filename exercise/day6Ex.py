# exercise 1
file = open("essay.txt",'w')
file.write("The true meaning of obscurity lies underneath the most "
           "delicate structures of viscosity. The idea of changing "
           "that balance is obscure by itself.")
file.close()
file = open("essay.txt",'r')
f = file.read()
print(f.title())

# exercise 2
file = open("essay.txt",'r')
no_char = file.read()
print(len(no_char))

# exercise3
file = open("members.txt",'w')
file.write("John Smith"+"\n"
           "Sen Lakmi "+"\n"
           "Sono Octonot"+"\n")
file.close()
# print(list(file))
member = input("Add a new member: ") + "\n"

file = open("members.txt",'r')
existing_member = file.readlines()
file.close()

existing_member.append(member + "\n")

file = open('members.txt', 'w')
existing_member = file.writelines(existing_member)
file.close()

file = open("members.txt",'r')
ff = file.read()
for i, in ff:
    print(i)


# exercise 4
filenames = ["doc.txt","doc2.txt","doc3.txt"]
for filename in filenames:
    file = open(filename,'w')
    file.write("Hellow")
    file.close()

# exercise 5
for filename in filenames:
    file = open(filename,'r')
    ff = file.read()
    print(ff)