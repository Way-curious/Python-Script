birthdays = {'Way': 'January', 'Win': 'January','Lu': 'September','Trang': 'June'}

while True:
    name = input('Pls enter the name(Type "x" to stop): ')
    if name == 'x':
        break
    if name in birthdays:
        print (birthdays[name] + ' is the birthday of ' + name  )
    else:
        print ("Don't have the birth day of " + name + " in the memory")
        print ("What is their birthday? ")
        bday = input()
        birthdays[name] = bday
        print ('Birthday database updated')

