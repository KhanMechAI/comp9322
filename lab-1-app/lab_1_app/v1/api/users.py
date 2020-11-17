# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from flask_restx import Resource, Namespace, reqparse
from v1.helpers.users import get_users, add_user
from v1.models import User
from v1.models.api_models import user_model, users_model

api = Namespace('user', description='access user resource')

api.models[user_model.name] = user_model
api.models[users_model.name] = users_model


user_parser = reqparse.RequestParser()
user_parser.add_argument("email", type=str, required=True)
user_parser.add_argument("first_name", type=str, required=True)
user_parser.add_argument("last_name", type=str, required=True)

@api.route('')
class UserQuery(Resource):
    @api.response(200, "Success")
    @api.doc(
        model=users_model,
        description="Detailed user details"
    )
    @api.marshal_with(users_model,)
    def get(self, ):
        payload = get_users()
        return {"users":payload}, 200

    @api.marshal_with(user_model)
    @api.doc(
        model=user_model,
        body=user_model,
    )
    @api.expect(user_parser)
    def post(self):
        payload = user_parser.parse_args()
        if User.query.with_entities(User.email).filter_by(email=payload['email']).first():
            return payload, 200
        user = add_user(payload)
        return user, 201
