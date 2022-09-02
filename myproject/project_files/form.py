from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class City(FlaskForm):
  name = StringField('City name', validators=[DataRequired(), Length(max=30)])
  submit = SubmitField('Send')