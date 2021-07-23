import datetime
now = datetime.datetime.now()

print("The current date and time is: ")
print(now.strftime('%Y-%m-%d ; %H:%M:%S'))
print(now.strftime('%H:%M:%S ; %A %B %d, %Y'))



calc = input("Enter your arithmetic operation:\n")
    
print("Your answer is: " + str(eval(calc)))

