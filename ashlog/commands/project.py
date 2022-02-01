import click
import requests
from common.util import (
    is_logged_in,
    get_access_token,
    get_host,
    send_get_request,
    send_post_request,
)
from urllib.parse import urljoin


@click.group()
def project():
    pass


@project.command()
def list():
    """ List all projects. """
    if is_logged_in():
        projects = send_get_request('api/project/')
        for project in projects:
            project_name = project['name']
            project_id = project['id']
            click.echo(f'{project_name}#{project_id}')


@project.command()
def new():
    """ Create a new project. """
    if is_logged_in():
        project_name = click.prompt('Project name', type=str)
        r = send_post_request(
            'api/project/',
            data={
                'name': project_name,
            },
        )
        print(r.content)
    else:
        click.echo('You must be logged in to create a project.', err=True)
