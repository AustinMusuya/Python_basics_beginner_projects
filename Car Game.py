# simple car game using while loop, if ..else statements

command = ''

while True:
    command = input('>:')
    if command == 'start':
        print(" Car has Started...")
    elif command == 'stop':
        print("Car is stopping...")
    elif command == 'help':
        print('''
        Instructions:
        To start the car - type start
        To stop the car - type stop
        To end the program - type quit
        
         enjoy the ride ;)
        ''')
    elif command == 'quit':
        break
    else:
        print('Invalid choice, try typing help for further instructions')
