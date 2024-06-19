from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField, ValidationError, TextAreaField,SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from ntb_marine.models import FileCategory
from flask_wtf.file import FileField, FileAllowed

class TemplateSearchForm(FlaskForm):
    searchtext = StringField('検索テキスト')
    submit = SubmitField('検索')

class SignatureForm(FlaskForm):
    ship_id = SelectField('船名', coerce=int, validators=[DataRequired(message="船名を選択してください")])
    template_id = IntegerField(validators=[DataRequired(), NumberRange(min=1, message="有効なテンプレートIDがありません")])
    signature = StringField('署名', validators=[DataRequired(message="署名を入力してください")])
    submit = SubmitField('書類作成')
    temp_file_path = StringField('temp_file_path')
    document_id = IntegerField('document_id')    

# class SignatureForm(FlaskForm):
#     ship_id = IntegerField('船名',validators=[DataRequired(), NumberRange(min=1, message="船名を選択してください")])
#     template_id = IntegerField(validators=[DataRequired(), NumberRange(min=1, message="有効なテンプレートIDがありません")])
#     signature = StringField('署名', validators=[DataRequired(message="署名を入力してください")])
#     submit = SubmitField('書類作成')        