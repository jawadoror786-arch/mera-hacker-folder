import random
name = input("Tumhara naam likho: ")
num = random.randint(100,999)
chars = "@#$!"
sp = random.choice(chars)
pas = name + str(num) + sp + "Ror"
print("Tumhara VIP Password:", pas)
