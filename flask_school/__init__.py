# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/01/24 00:48:18
'''
from school_sdk import SchoolClient, UserClient


class School(object):
    school:SchoolClient = None

    def __init__(self, app) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        school_sdk_config = app.config.get('SCHOOL_SDK_CONFIG', None)

        self.school = SchoolClient(**school_sdk_config)
        app.extensions['school'] = self.school

    def user_login(self, account:str, password:str, **kwargs):
        user = UserClient(self.school, account=account,password=password)
        return user.login()
    
    def dev_user(self, cookies:str = None):
        dev_user = UserClient(self.school)
        return dev_user.get_dev_user(cookies)