# -*- coding: utf-8 -*-

from flask import Blueprint

# blueprint
user = Blueprint('user', __name__)


@user.route('/v1/user/get')
def get_user():
    return 'I am John'
