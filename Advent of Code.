commands = user_input.strip().split('\n')
count = 0
for command in commands:
    startingLetter = command[0]
    value_str = command[1:]
    value = int(value_str)
    
    if (startingLetter == "R"):
        tracking_num = (tracking_num + value) % 100
    elif (startingLetter == "L"):
        tracking_num = (tracking_num - value) % 100 
    if (value % 100 == 0):
        count += 1 
print(count)
