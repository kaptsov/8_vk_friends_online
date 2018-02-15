import vk


APP_ID = 6371981


def get_user_login():
    return input('login:')


def get_user_password():
    return input('password:')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends",
    )
    api_context = vk.API(session)
    friends_online_id_list = api_context.friends.getOnline()
    return api_context.users.get(user_ids=friends_online_id_list)


def output_friends_to_console(friends_online):
    print('Look, who is online:\n')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except(vk.exceptions.VkAuthError):
        exit('Wrong login or password.')
