from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'pylearn'}
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column('login', db.String(50), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.Text)
    role=db.Column(db.String(50), index=True, default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_id(self):
        return str(self.id_user)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Module(db.Model):
    __tablename__ = 'modules'
    __table_args__ = {'schema': 'pylearn'}
    id_module = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50))

    description = db.Column(db.Text)

    image_path = db.Column(db.Text, default='default_course.jpg')

    def __repr__(self):
        return f'<Course {self.name}>'

    def get_id(self):
        return str(self.id_module)

class Lesson(db.Model):
    __tablename__ = 'lessons'
    __table_args__ = {'schema': 'pylearn'}
    id_lesson = db.Column(db.Integer, primary_key=True)

    topic = db.Column(db.String(50))

    content = db.Column(db.Text)

    id_module = db.Column(db.Integer)

    def __repr__(self):
        return f'<Lesson {self.title}>'

    def get_id(self):
        return str(self.id_lesson)

class Quiz(db.Model):
    __tablename__ = 'quiz'
    __table_args__ = {'schema': 'pylearn'}
    id_quiz = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    id_lesson = db.Column(db.Integer)
    submitted = db.Column(db.Boolean, default=False)

class Question(db.Model):
    __tablename__ = 'question'
    __table_args__ = {'schema': 'pylearn'}
    id_question = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    id_quiz = db.Column(db.Integer)

class Answer(db.Model):
    __tablename__ = 'answer'
    __table_args__ = {'schema': 'pylearn'}
    id_answer = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
    is_right = db.Column(db.Boolean, default=False)

class User_Answer(db.Model):
    __tablename__ = 'user_answer'
    __table_args__ = {'schema': 'pylearn'}
    id_answer = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))