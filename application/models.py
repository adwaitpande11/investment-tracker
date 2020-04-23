from application import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(20), nullable=False)
    user_middle_name = db.Column(db.String(20))
    user_last_name = db.Column(db.String(20))
    user_email_id = db.Column(db.String(100), unique=True, nullable=False)
    user_phone_no = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self) -> str:
        return '[user_id=' + str(self.user_id) + ', user_first_name=' + self.user_first_name + ', user_last_name='\
               + self.user_last_name + ']'
