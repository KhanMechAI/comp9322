# -*- coding: utf-8 -*-
from __future__ import absolute_import
from pathlib import Path

from flask import Flask

from v1.models import db
from v1 import api


def boot_app(app):

    db_path = Path(app.instance_path) / "lab_1.db"
    print(db_path)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=db_path,
        SQLALCHEMY_DATABASE_URI="sqlite:///" + str(db_path),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(api)

    boot_app(app)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)