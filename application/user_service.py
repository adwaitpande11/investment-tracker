import re

from application import bcrypt, db
from application.models import User


class UserService:
    def save_user(self, payload):
        if self.validate_user_registration_data(payload):
            user = User()
            user.user_first_name = payload.get('user_first_name')
            user.user_middle_name = payload.get('user_middle_name')
            user.user_last_name = payload.get('user_last_name')
            user.user_email_id = payload.get('user_email_id')
            user.user_phone_no = payload.get('user_phone_no')
            user.password = bcrypt.generate_password_hash(payload.get('password')).decode('utf-8')
            db.session.add(user)
            db.session.commit()
            return user
        return False

    def validate_user_registration_data(self, user_data):
        if not user_data.get('user_first_name'):
            return False

        if not user_data.get('user_last_name'):
            return False

        if not re.search(r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,4})+$', user_data.get('user_email_id')):
            return False

        if not user_data.get('user_phone_no'):
            return False

        if not user_data.get('password'):
            return False

        return True
