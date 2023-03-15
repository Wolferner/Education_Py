class User:
    def __init__(self, group: str):
        self.group = group


if __name__ == '__main__':
    user = User('admin')

    if user.group == 'admin':
        process_admin_request(user, request)
    elif user.group == 'manager':
        process_manager_request(user, request)
    elif user.group == 'client':
        proces_client_request(user, request)

    group_to_process_method = {
        'admin': process_admin_request,
        'manager': process_manager_request,
        'client': proces_client_request
    }

    group_to_process_method['admin'](user, request)