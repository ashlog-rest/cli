import click
from ashlog.commands.auth import auth
from ashlog.commands.project import project
import pkg_resources


@click.group()
@click.version_option(
    pkg_resources.require('ashlog-cli')[0].version
)
@click.pass_context
def cli(ctx):
    pass


cli.add_command(auth)
cli.add_command(project)
