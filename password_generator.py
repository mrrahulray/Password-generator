#password generator

#Version 1.0

import random
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '_', '+', '-', '=', '{', '}', '[', ']', '\\', '|', 
    ';', ':', '"', "'", '<', '>', ',', '.', '?', '/'
]
numbers=[0,1,2,3,4,5,6,7,8,9]


latters_count =int(input("how many latters do you want in your password: "))
numbers_count =int(input("how many numbers do you want in your password: "))
symblols_count =int(input("how many simbles do you want in your password: "))


password_list=[]


for i in range(0,latters_count):
    if random.randint(0,1)==1:
        password_list.append((random.choice(alphabets)).lower())
    else:
        password_list.append((random.choice(alphabets)))


for i in range(0,numbers_count):
    password_list.append(str(random.choice(numbers)))

for i in range(0,symblols_count):
    password_list.append(random.choice(symbols))

# Shuffle the password list to ensure randomness
random.shuffle(password_list)

password= ""
for i in password_list:
    password+=i
print(f"The generated password: {password}")




