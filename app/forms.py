from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired

class AddVisitForm(FlaskForm):
    visit_ID = StringField('Visit ID', validators=[])
    patient_ID = StringField('Pateint Number',validators=[])
    thc_number = StringField('TBH #',validators=[])
    date = StringField('Date',validators=[])