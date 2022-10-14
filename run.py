def welcome_user():

    username = None
    
    while True:
        username = input('Enter your name\n')
        if not username.isalpha():
            print('Username must be alphabets only')
            continue
        else:
            print(f'welcome {username}')
            break

    print('Welcome to Hangman')
    welcome_user()