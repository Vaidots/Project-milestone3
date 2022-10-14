def welcome_user():

    username = None
    
    while True:
        username = input('Enter your name\n')
        if not username.isalpha():
            print('Username must be alphabets only')
            continue