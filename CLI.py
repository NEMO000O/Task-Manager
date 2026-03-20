from pathlib import Path
import click

"""Простой менеджер задач"""

@click.command()
@click.argument("file",
               type=click.File(mode="a"),
               )
def cli(file):
    task = input()
    file.write(f"{task}\n")

if __name__ == "__main__":
    cli()
