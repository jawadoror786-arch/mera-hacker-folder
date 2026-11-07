import random, string
chars = string.ascii_letters + string.digits + "@#$!"
pas = "".join(random.choice(chars) for i in range(12))
print("Tumhara Strong Password:", pas)
