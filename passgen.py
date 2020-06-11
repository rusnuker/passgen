import random,sys 

chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890-_+=;.,"
password = ""

if len(sys.argv) != 2:
	print("usage: passgen.py LENGTH - prints password with custom length.")
	raise SystemExit
if sys.argv[1].isdigit() == False:
	print("You should set number. " + sys.argv[0] + " returned error.")
	raise SystemExit

for n in range(int(sys.argv[1])):
	password = password + chars[random.randint(0, len(chars)-1)]
	n = n+1

print("Your password is \n\n" + password)

# Hey man! It's code for generate strong password. But you can say: "No, this password isn't strong
# because this code returns pseudo-random line of chars!" Yes, it is. But for social network it's good!

# I was killed for this code one hour of my life! Sh1t!