import requests
class Yaris:
    def __init__(self):
        self.public_auth_key = None
        self.private_auth_key = None
    
    def set_private_key(self, key):
        self.private_auth_key = key
    
    def set_public_key(self, key):
        self.public_auth_key = key
    
    def get_wl_info(self):
        headers = {'yaris-authentication': self.private_auth_key}
        r = requests.post(f'https://yaris.rocks/api/v1/', headers=headers)
        return r.json()

    def add_user(self, username, password, role):
        headers = {'yaris-authentication': self.private_auth_key}
        params = {'username': username, 'password': password, 'role': role}
        r = requests.post('https://yaris.rocks/api/v1/add', headers=headers, json=params)
        return r.json()
    
    def remove_user(self, username):
        headers = {'yaris-authentication': self.private_auth_key}
        params = {'username': username}
        r = requests.post('https://yaris.rocks/api/v1/remove', headers=headers, json=params)
        return r.json()
    
    def whitelist_user(self, username):
        headers = {'yaris-authentication': self.private_auth_key}
        params = {'username': username}
        r = requests.post('https://yaris.rocks/api/v1/whitelist', headers=headers, json=params)
        return r.json()
    
    def blacklist_user(self, username, reason):
        headers = {'yaris-authentication': self.private_auth_key}
        params = {'username': username, 'reason': reason}
        r = requests.post('https://yaris.rocks/api/v1/blacklist', headers=headers, json=params)
        return r.json()
    
    def log_in(self, username, password):
        params = {'username': username, 'password': password}
        r = requests.get(f'https://yaris.rocks/access/?apikey={self.public_auth_key}', params=params)
        return r.json()
