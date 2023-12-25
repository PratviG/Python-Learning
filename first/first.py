student = ["ram", "radha", "shyam", "kishan", "radhika"]
print(student[1])

print(len(student))

print(student[len(student)-1])

name = "Tejas Gondaliya"
name2 = "Gondaliya Tejas"
name3 = "gelani Pratvi"


# name = ["Tejas Gondaliya", "Gondaliya Tejas", "gelani Pratvi"]

print(len(name))

print(name[-1])

if name in "Tejas":
    print(True)
else:
    print(False)
print(True if "Tejas" in name3 else False)

print(name[0:5:1])

# length_name = len(student)-1
# for i in range(length_name):
#     print(student[i])
#
# for i in student:
#     print(i)

# for i in range(10):
#     if i>5:
#         break
#     print(i)


# a = 0
# while True:
#     print(a)
#     a+=1

# b = 0
# while(b<5):
#     print(b)
#     b+=1