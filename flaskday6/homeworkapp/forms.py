from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class User(FlaskForm):
    name = StringField(label="用户名",validators=[DataRequired()])
    password = StringField(label="密码", validators=[DataRequired()])
    submit = SubmitField(label="点击登录")

