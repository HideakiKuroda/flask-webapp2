from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField, ValidationError, TextAreaField,SelectField
from wtforms.validators import DataRequired
from ntb_marine.models import FileCategory
from flask_wtf.file import FileField, FileAllowed

class TemplateSearchForm(FlaskForm):
    searchtext = StringField('検索テキスト')
    submit = SubmitField('検索')