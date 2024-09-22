import getpass
database = {'admin':'admin123', 'user1':'user123', 'user2':'user123'}

user = input('Enter username: ')
password = getpass.getpass('Enter password: ')

userFound = False
maxAttempts = 3
falseCount = 0
loggedIn = False

for i in database.keys():
    if user == i:
        userFound = True
        while password != database.get(i) and falseCount < maxAttempts:
            password = getpass.getpass(f'Incorrect password! You have {maxAttempts - falseCount} attemps left. Try Again: ')
            if password != database.get(i):
                falseCount += 1
            else:
                loggedIn = True
        break

if not userFound:
    print('User not found!')
elif falseCount == maxAttempts:
    print('Too many incorrect attempts. Try again later.')
elif loggedIn:
    print('Login Successful!')
else:
    print('Login Failed!')