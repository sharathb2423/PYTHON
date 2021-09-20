import random

print('\n' * 30  + ' ' * 60 + 'WELCOME TO SCRIPTERS!')
master_password = 'MASTER_PWD'
connect = input('\nEnter the master password: ')
while master_password != connect:
    connect = input('Enter the master password: ')
print('\nYou have a scripters account!')
print('What would you like to store in today?')

while True:
    mode = input('\n\nWhat would you like to do? choose an option'
                '\n1. Insert a new password'
                '\n2. Find the password of an app'
                '\n3. Generate a random password'
                '\n4. View all the passwords stored'
                '\n5. Exit the current program ')

    if mode == '1':
        software = input('\nEnter the name of the app or software: ')
        username = input('Enter the username for your ' + software + ' account: ')
        account = input('Provide a user email for this app or software: ')
        while '@' not in account:
            print('Enter a valid email id!')
            account = input('Provide a user email for this app or software: ')
        password = input('Enter the password for your ' + software + ' account: ')
        while len(password) < 5:
            print('Passwords must at least have 5 characters!')
            password = input('Enter the password for your ' + software + ' account: ')
        file = open('password.txt', 'a')
        file.write(software + ' | ' + username + ' | ' + account + ' | ' + password + ' | ' + 'www.' + software.lower() + '.com' + '\n')
        file.close()

    if mode == '2':
        ask_app = input('\nEnter the name of the app or software that you want to view your password: ')
        with open('password.txt', 'r') as file:
            for line in file.readlines():
                if line.startswith(ask_app):
                    def show_pass():
                        string = (line.split())
                        return string[-3]
                    print('Software: ' + ask_app + '  |  Password: ' + show_pass())

    if mode == '3':
        password_len = input('Enter how long your password should be: ')
        if password_len.isdigit(): password_len = int(password_len)
        else: print('The length of the password should be in numbers: ')
        password = ''
        for i in range(password_len // 2):
            i = chr(random.randint(65, 90)).upper()
            j = chr(random.randint(65, 90)).lower()
            for s in range(1):
                s = chr(random.randint(65, 90)).lower()
            password = str(password) + i + j
        print('The ganerated password is ' + str(password))
    
    if mode == '4':
        with open('password.txt', 'r') as file:
            print('\n')
            for line in file.readlines():
                data = line.rstrip()
                print(data)
    if mode == '5': break