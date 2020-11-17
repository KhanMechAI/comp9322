from flask_restx import Model, fields


email = fields.String(required=True, description="User email", example="test@test.com")

first_name = fields.String(
    required=True, description="User first name", example="Brett"
)

last_name = fields.String(required=True, description="User last name", example="Lee")

user_model = Model(
    "User",
    {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    }
)

users_model = Model(
    "Users",
    {
        'users': fields.List(fields.Nested(user_model))
    }
)