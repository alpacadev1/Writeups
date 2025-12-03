'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
tracking_num = 50 

user_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

commands = user_input.strip().split('\n')
count = 0
for command in commands:
    startingLetter = command[0]
    value_str = command[1:]
    value = int(value_str)
    
    if (value // 100 >= 1):
        count += value // 100
        value = value % 100
    
    if (startingLetter == "R"):
        if (tracking_num + value > 100 and tracking_num != 0):
            count += 1
        tracking_num = (tracking_num + value) % 100
    elif (startingLetter == "L"):
        if (tracking_num - value < 0 and tracking_num != 0):
            count += 1
        tracking_num = (tracking_num - value) % 100 
    if (tracking_num % 100 == 0):
        count += 1 
print(count)
