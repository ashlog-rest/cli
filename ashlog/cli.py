import click
from ashlog.commands.auth import auth
from ashlog.commands.project import project
from ashlog.__meta__ import __version__


@click.group()
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    pass


cli.add_command(auth)
cli.add_command(project)
