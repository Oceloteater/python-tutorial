import functools

user = {'name': 'Adam', 'age': 31, 'access_level': 'admin'}


# passing a function to another function (called decorator function - I'd call it a wrapper func)
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No permissions for {user["name"]}'
        return secure_function
    return decorator


@make_secure('admin')  # does this - get_admin_password = make_func_secure(get_admin_password)
def get_admin_password(panel):
    return 'Admin user - 12345678'


@make_secure('guest')
def get_dashboard_password():
    return 'User guest - password1'


print(get_admin_password('admin'))
print(get_dashboard_password('guest'))
