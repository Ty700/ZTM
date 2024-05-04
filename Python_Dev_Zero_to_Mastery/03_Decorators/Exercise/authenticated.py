# Create an @authenticated decordator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True, # Changing this to false will either run or not run the message_friends function
}

def authernicated(fn):
    def wrapper(*args, **kwargs):
        if user1['valid'] == True:
            fn(*args, **kwargs)
    return wrapper


@authernicated
def message_friends(user):
    print('message has been sent')

message_friends(user1)