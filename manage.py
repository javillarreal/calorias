import json
#import click
from flask.cli import FlaskGroup
import settings
from app import app, db

cli = FlaskGroup(app)

@cli.command('create-db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('commit')
def create_food_image():
    db.session.commit()

if __name__ == '__main__':
    cli()
