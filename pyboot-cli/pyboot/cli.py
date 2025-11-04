import click
from .commands.create import create

@click.group()
@click.version_option()
def cli():
    """PyBoot - A CLI tool to bootstrap Python projects"""
    pass

# 添加 create 命令
cli.add_command(create)

if __name__ == "__main__":
    cli()