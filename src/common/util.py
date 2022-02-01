import keyring
import os
import requests
from urllib.parse import urljoin

ashlog_dir = os.path.join(os.path.expanduser('~'), '.ashlog')


def is_logged_in():
    """ Check if username and password are in keyring """
    credentials = keyring.get_credential('ashlog', None)
    if credentials is not None:
        return True
    else:
        return False


def get_credential():
    """ Returns username and password """
    credential = keyring.get_credential('ashlog', None)
    return credential.username, credential.password


def get_host():
    """ Return host """
    with open(os.path.join(ashlog_dir, 'host')) as f:
        return f.read()


def get_access_token():
    """ Return access token """
    if is_logged_in():
        username, password = get_credential()
        r = requests.post(
            urljoin(get_host(), 'auth/token/'),
            json={
                'username': username,
                'password': password,
            },
        )
        return r.json()['access']


def send_post_request(endpoint, data):
    return requests.post(
        urljoin(get_host(), endpoint),
        json=data,
        headers={'Authorization': f'Bearer {get_access_token()}'}
    )


def send_get_request(endpoint, data=None):
    return requests.get(
        urljoin(get_host(), endpoint),
        json=data,
        headers={'Authorization': f'Bearer {get_access_token()}'}
    )
