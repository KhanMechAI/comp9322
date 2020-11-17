# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask_restx import Api
from flask import Blueprint


from .users import api as ns1



blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


# All API metadatas
api = Api(
    blueprint,
    title="Lab 1 API",
    version="0.01",
    description="Demo API",
)

api.add_namespace(ns=ns1, path="/users")