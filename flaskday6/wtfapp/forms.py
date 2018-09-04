from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    proname = StringField(label="产品名称",validators=[DataRequired()])
    submit = SubmitField(label="点击提交")

