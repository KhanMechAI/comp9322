from v1.models import User, db


def get_users():
    payload = [u.__dict__ for u in User.query.all()]

    return payload

def add_user(user_dict):
    try:
        new_user = User(
            first_name=user_dict["first_name"],
            last_name=user_dict["last_name"],
            email=user_dict["email"],
        )
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return 400
    return user_dict