from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, validators
from wtforms.validators import DataRequired

class AddVisitForm(FlaskForm):
    visit_ID = IntegerField('Visit ID', validators=[DataRequired()])
    patient_ID = IntegerField('Pateint Number',validators=[DataRequired()])
    thc_number = IntegerField('TBH #',validators=[DataRequired()])
    date = DateField('Date',validators=[DataRequired()], format = '%Y-%m-%d')
    submit = SubmitField('Submit')
from wtforms import StringField, IntegerField, DateField, BooleanField, TextAreaField, validators
from wtforms.validators import DataRequired, Required

class AddVisitForm(FlaskForm):
    visit_ID = StringField('Visit ID', validators = [])
    patient_ID = StringField('Pateint Number',validators = [])
    thc_number = IntegerField('THC #',validators = [])
    date = DateField('Date',validators = [])

class AddInterviewForm(FlaskForm):
    visit_ID = StringField('Visit ID', validators = [])
    date = DateField('Date', validators = [])
    thc_number = IntegerField('THC #', validators = [])
    patient_ID = StringField('Patient Number', validators = [])
    visit_number = IntegerField('Visit No.', validators = [])

class AddInitialInterviewForm(FlaskForm):
    # Beginning info
    clinic_number = IntegerField('Clinic #:', validators = [])
    first_name = StringField('First Name:', validators = [])
    last_name = StringField('Last Name:', validators = [])
    dob = DateField('DOB:', validators = [])
    ssn = IntegerField('SSN:', validators = [])
    insurance = StringField('Insurance:', validators = [])
    date = DateField('Date:', validators = [])
    thc = IntegerField('T&HC:', validators = [])
    telephone = IntegerField('Telephone:', validators = [])
    email = StringField('Email:', validators = [])

    ''' TINNITUTS '''
    re = BooleanField('RE', validators = [])
    le = BooleanField('LE', validators = [])
    both = BooleanField('Both', validators = [])
    head = BooleanField('Head', validators = [])
    intermittent = BooleanField('Intermittent', validators = [])
    constant = BooleanField('Constant', validators = [])

    gradual = BooleanField('Gradual', validators = [])
    sudden = BooleanField('Sudden', validators = [])
    when = StringField('When', validators = [])
    fluctuations_volume_yes = BooleanField('Yes', validators = [])
    fluctuations_volume_no = BooleanField('No', validators = [])
    description_t_sound = TextAreaField('Description of T sound(s):', validators = [])

    # Activities prevented
    concentration_t_init = BooleanField('Concentration', validators = [])
    sleep_t_init = BooleanField('Sleep', validators = [])
    qra_t_init = BooleanField('QRA', validators = [])
    work_t_init = BooleanField('Work', validators = [])
    restaurants_t_init = BooleanField('Restaurants', validators = [])
    sports_t_init = BooleanField('Sports', validators = [])
    social_t_init = BooleanField('Social', validators = [])
    other_t_init = BooleanField('Other', validators = [])

    # % of time when
    aware_t_init = IntegerField('Aware', validators = [])
    annoyed_t_init = IntegerField('Annoyed', validators = [])
    severity_t_init = IntegerField('Severity', validators = [])
    annoyance_t_init = IntegerField('Annoyance', validators = [])
    effectonlife_t_init = IntegerField('Effect on Life', validators = [])

    # Bad Days 
    baddays_yes_t_init = BooleanField('Yes', validators = [])
    baddays_no_t_init = BooleanField('No', validators = [])
    baddays_freq_t_init = IntegerField('Frequency', validators = [])

    # Effect of Sound
    none_t_init = BooleanField('None', validators = [])
    louder_t_init = BooleanField('Louder', validators = [])
    softer_t_init = BooleanField('Softer', validators = [])
    mins_t_init = BooleanField('Mins', validators = [])
    hours_t_init = BooleanField('Hours', validators = [])
    days_t_init = BooleanField('Days', validators = [])

    # Ear overprotection
    overprotection_yes_t_init = BooleanField('Yes', validators = [])
    overprotection_no_t_init = BooleanField('No', validators = [])
    overprotection_freq_t_init = IntegerField('Percent of time when', validators = [])    
    quiet_yes_t_init = BooleanField('Yes', validators = [])
    quiet_no_t_init = BooleanField('No', validators = []) 

    # Comments
    comments_spec_t_init = StringField('Any other T specific treatments:', validators = [])
    problem_t_init = StringField('Why is T a problem?', validators = [])   
    
    




    
