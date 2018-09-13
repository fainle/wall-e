#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from web_core import create_app
from flask.cli import AppGroup


app = create_app()
user_cli = AppGroup('user')


@user_cli.command('create')
@click.argument('name')
def create_user(name):
    pass


app.cli.add_command(user_cli)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12000)