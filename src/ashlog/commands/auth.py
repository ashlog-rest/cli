import click
import keyring
import os
import requests
from urllib.parse import urljoin
from common.util import ashlog_dir, get_credential, is_logged_in


@click.group()
def auth():
    pass


@auth.command()
def login():
    """ Check credentials and store it in keyring. """
    if is_logged_in():
        click.echo('You are already logged in.', err=True)
    else:
        host = click.prompt('AshLog host', type=str)
        username = click.prompt('Username', type=str)
        password = click.prompt('Password', type=str, hide_input=True)
        r = requests.post(
            urljoin(host, 'auth/token/'),
            json={
                'username': username,
                'password': password,
            }
        )
        if r.status_code == 200:
            ashlog_dir_exists = os.path.exists(ashlog_dir)
            if not ashlog_dir_exists:
                os.makedirs(ashlog_dir)
            with open(os.path.join(ashlog_dir, 'host'), 'w') as f:
                f.write(host)
            keyring.set_password('ashlog', username, password)
            click.echo('Successfully logged in!')
        else:
            click.echo(
                'There was an error with your request. Please check your inputs and try again,', err=True)


@auth.command()
def logout():
    """ Remove credentials from keyring. """
    if is_logged_in():
        username = get_credential()[0]
        keyring.delete_password(
            'ashlog', username)
    else:
        click.echo('You are not logged in.', err=True)


@auth.command()
def whoami():
    """ Return the username of the logged in user. """
    if is_logged_in():
        username = get_credential()[0]
        click.echo(f'Logged in as {username}.')
    else:
        click.echo('You are not logged in.', err=True)
