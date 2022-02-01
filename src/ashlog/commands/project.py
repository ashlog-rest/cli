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
        r = send_get_request('api/project/')
        if r.status_code == 200:
            for project in r.json():
                project_name = project['name']
                project_id = project['id']
                click.echo(f'{project_name}#{project_id}')
        else:
            click.echo('There was an error with your request.', err=True)


@project.command()
@click.argument('project_id')
def logs(project_id):
    """ List all logs in project. """
    if is_logged_in():
        r = send_get_request(
            f'api/project/{project_id}/log/',
        )
        if r.status_code == 200:
            for log in r.json():
                log_event = log['event']
                log_created = log['created']
                print(f'[{log_created}] {log_event}')
        else:
            click.echo('There was an error with your request.', err=True)
    else:
        click.echo('You must be logged in to display the logs.', err=True)


@project.command()
@click.argument('project_name')
def new(project_name):
    """ Create a new project. """
    if is_logged_in():
        r = send_post_request(
            'api/project/',
            data={
                'name': project_name,
            },
        )
        if r.status_code == 201:
            project_id = r.json()['id']
            click.echo(
                f'Project {project_name}#{project_id} has been created.')
        else:
            click.echo(
                'There was an error while creating the project.', err=True)
    else:
        click.echo('You must be logged in to create a project.', err=True)
