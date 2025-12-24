from flask import Blueprint, render_template
from .models import Module

main = Blueprint('main', __name__)

@main.route('/')
def base():
    return render_template('base.html')

@main.route('/modules')
def modules():
    all_courses = Module.query.all()
    return render_template('modules.html')


@main.route('/login')
def login():
    return render_template('login.html')