# -*- coding: utf-8 -*-
'''
    :file: app.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/01/24 13:11:33
'''
from flask import Flask

from flask_school import School


app = Flask(__name__)

app.config['SCHOOL_SDK_CONFIG'] = {
    # 教务系统URL
    "host": "192.168.2.123",
    # 端口
    "port": 7899,
    # 是否需要验证码
    "exist_verify": True,
    # 验证码类型(kap: 数字验证 | cap: 滑块验证)
    "captcha_type": 'kap'
}

school = School(app)

@app.get("/<account>/<password>")
def get_info(account, password):
    user = school.user_login(account, password)
    return user.get_info()