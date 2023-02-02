from os import system
import time


choice = ''


def palidrome_check(text) -> None:
    temp = ''
    for a in text:
        temp = a + temp

    if temp == text:
        print(f'Plain text: {text}\nReversed text: {temp}\n\nConclusion - is palidrome.')
    else:
        print(f'Plain text: {text}\nReversed text: {temp}\n\nConclusion - is NOT palidrome.')

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
        for i in range(1, peak + 1):
            print('* ' * i)
        for a in range(peak - 1, 0, -1):
            print('* ' * a)
    elif choice == '2':
        print('Welcome to series of 5')
        number = int(input('Insert number: '))
        summary = 0
        temp = ''
        for g in range(1, number + 1):
            temp = '5' * g
            summary += int(temp)
            if g < number:
                print(f'{temp} + ', end='')
            elif g == number:
                print(f'{temp} ', end='')
        print(f'= {summary}')
    elif choice == '3':
        user_data = int(input("Give an edge number: "))
        for h in range(1, user_data + 1):
            print(f'Current number: {h} and the cube is {h ** 3}')
    elif choice == '4':
        plain_text = input('Insert your string: ')
        palidrome_check(plain_text)
    elif choice == '5':
        sequence = input('Insert your sequence which each word separated with hyphen: ')
        unsorted_items = []
        for item in sequence.split('-'):
            unsorted_items.append(item)
        
        unsorted_items.sort()
        print('-'.join(unsorted_items))
    if choice != 'x':
        print()
        input('Press Enter to continue...')
        continue
    else:
        system('clear')
        print("Alright, see you!")