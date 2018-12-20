import click
from sayhello import app, db


@app.cli.command()
def initdb():
    db.drop_all()
    db.create_all()
    click.echo('Database initialized.')
