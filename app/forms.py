from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, validators
from wtforms.validators import DataRequired

class AddVisitForm(FlaskForm):
    visit_ID = IntegerField('Visit ID', validators=[DataRequired()])
    patient_ID = IntegerField('Pateint Number',validators=[DataRequired()])
    thc_number = IntegerField('TBH #',validators=[DataRequired()])
    date = DateField('Date',validators=[DataRequired()], format = '%Y-%m-%d')
    submit = SubmitField('Submit')