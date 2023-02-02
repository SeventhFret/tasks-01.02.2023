from os import system

choice = ''


while choice != 'x':
    system('clear')
    print('''What you want to do?
[1] - Task 1
[2] - Task 2
[3] - Task 3
[4] - Task 4
[5] - Task 5
[x] - Exit
''')
    choice = input()
    print()
    if choice == '1':
        peak = int(input('Input your peak amount of asteriscs: '))

        for i in range(peak):
            pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    if choice != 'x':
        print()
        input('Press Enter to continue...')
        continue
    else:
        print("Alright, see you!")