database = [
    {'username': 'RobStark', 'password': hash('1234test')},
    {'username': 'JhonSnow', 'password': hash('19283746')},
    {'username':'SansaStark', 'password': hash('87654321')}
]

def in_database(username: str) -> bool:
    for user in database:
        if user['username'] == username:
            return True
    return False

def get_user(username: str, password: str) -> dict:
    if not in_database(username):
        raise Exception('user is not found')
    for user in database:
        if user['username'] == username:
            if user['password'] != hash(password):
                raise Exception('password is wrong')
            else:
                return user

def register(username: str, password: str, password_confirm: str) -> str:
    if in_database(username):
        raise Exception('name is not free')
    if password != password_confirm:
        raise Exception('passwords is not same')
    new_user = {'username': username, 'password': hash(password)}
    database.append(new_user)
    return 'you signed up'


def login(username: str, password: str) -> str:
    get_user(username, password)
    return 'you log in your account'


def change_password(username, password):
    user = get_user(username, password)
    new_password = input('enter the new password: ')
    index = database.index(user)
    user_from_db = database[index]
    user_from_db['password'] = hash(new_password)
    return 'password updated'


def delete_account(username: str, password: str):
    user = get_user(username, password)
    database.remove(user)
    return 'account deleted'





print(register('nurs','234565432','234565432'))
print(login('nurs','234565432'))
print(change_password('nurs','234565432'))
print(delete_account('nurs','234565432'))
rrrrrrrrrr


# da nu nahuy
