PASSWORD = "1234567"

def password_required(need):
    def wrapper():
        password = input('What is your password? ')
        
        if password == PASSWORD:
            return need()
        else:
            print('The password is not correct')
                 
    return wrapper

@password_required
def needs_password():
    print('The password is correct')
    
def upper(func):
    def wrapper(*args, ** kwargs):
        result = func(*args, **kwargs)
        
        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)


if __name__ == '__main__':
    print(say_my_name('Christian'))