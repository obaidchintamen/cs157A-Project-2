from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, validators
from wtforms.validators import DataRequired, InputRequired, NumberRange, Email, Optional
from wtforms import StringField, IntegerField, DateField, BooleanField, TextAreaField, validators
from wtforms.validators import DataRequired, Required

class AddVisitForm(FlaskForm):
    visit_ID = IntegerField('Visit ID', validators=[DataRequired()])
    patient_ID = IntegerField('Pateint Number',validators=[DataRequired()])
    thc_number = IntegerField('TBH #',validators=[DataRequired()])
    date = DateField('Date',validators=[DataRequired()], format = '%Y-%m-%d')
    submit = SubmitField('Submit')


class AddInterviewForm(FlaskForm):
    visit_ID = StringField('Visit ID', validators = [InputRequired()])
    date = DateField('Date', validators = [InputRequired()])
    thc_number = IntegerField('THC #', validators = [InputRequired()])
    patient_ID = StringField('Patient Number', validators = [InputRequired()])
    visit_number = IntegerField('Visit No.', validators = [InputRequired()])

class AddInitialInterviewForm(FlaskForm):
    # Beginning info
    clinic_number = IntegerField('Clinic #:', validators = [InputRequired()])
    first_name = StringField('First Name:', validators = [InputRequired()])
    last_name = StringField('Last Name:', validators = [InputRequired()])
    dob = DateField('DOB:', validators = [InputRequired()])
    ssn = IntegerField('SSN:', validators = [NumberRange(min = 000000000, max = 999999999, message = "SSN must be 9 digits")])
    insurance = StringField('Insurance:', validators = [InputRequired()])
    date = DateField('Date:', validators = [InputRequired()])
    thc = IntegerField('T&HC:', validators = [InputRequired()])
    telephone = IntegerField('Telephone:', validators = [InputRequired(), NumberRange(min = 0000000000, max = 9999999999, message = "Telephone number must be 10 digits")])
    email = StringField('Email:', validators = [InputRequired(), Email()])

    ''' TINNITUTS '''
    re = BooleanField('RE', validators = [Optional()])
    le = BooleanField('LE', validators = [Optional()])
    both = BooleanField('Both', validators = [Optional()])
    head = BooleanField('Head', validators = [Optional()])
    intermittent = BooleanField('Intermittent', validators = [Optional()])
    constant = BooleanField('Constant', validators = [Optional()])

    gradual = BooleanField('Gradual', validators = [Optional()])
    sudden = BooleanField('Sudden', validators = [Optional()])
    when = StringField('When', validators = [Optional()])
    fluctuations_volume_yes = BooleanField('Yes', validators = [Optional()])
    fluctuations_volume_no = BooleanField('No', validators = [Optional()])
    description_t_sound = TextAreaField('Description of T sound(s):', validators = [InputRequired()])

    # Activities prevented or affected
    concentration_t_init = BooleanField('Concentration', validators = [Optional()])
    sleep_t_init = BooleanField('Sleep', validators = [Optional()])
    qra_t_init = BooleanField('QRA', validators = [Optional()])
    work_t_init = BooleanField('Work', validators = [Optional()])
    restaurants_t_init = BooleanField('Restaurants', validators = [Optional()])
    sports_t_init = BooleanField('Sports', validators = [Optional()])
    social_t_init = BooleanField('Social', validators = [Optional()])
    other_t_init = BooleanField('Other', validators = [Optional()])

    # % of time when
    aware_t_init = IntegerField('Aware', validators = [InputRequired(), NumberRange(min = 0, max = 100, message = "Number must be between 0 and 100")])
    annoyed_t_init = IntegerField('Annoyed', validators = [InputRequired(), NumberRange(min = 0, max = 100, message = "Number must be between 0 and 100")])
    severity_t_init = IntegerField('Severity', validators = [InputRequired(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 100")])
    annoyance_t_init = IntegerField('Annoyance', validators = [InputRequired(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    effectonlife_t_init = IntegerField('Effect on Life', validators = [InputRequired(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])

    # Bad Days 
    baddays_yes_t_init = BooleanField('Yes', validators = [Optional()])
    baddays_no_t_init = BooleanField('No', validators = [Optional()])
    baddays_freq_t_init = IntegerField('Frequency', validators = [InputRequired()])

    # Effect of Sound
    none_t_init = BooleanField('None', validators = [Optional()])
    louder_t_init = BooleanField('Louder', validators = [Optional()])
    softer_t_init = BooleanField('Softer', validators = [Optional()])
    mins_t_init = BooleanField('Mins', validators = [Optional()])
    hours_t_init = BooleanField('Hours', validators = [Optional()])
    days_t_init = BooleanField('Days', validators = [Optional()])

    # Ear overprotection
    overprotection_yes_t_init = BooleanField('Yes', validators = [Optional()])
    overprotection_no_t_init = BooleanField('No', validators = [Optional()])
    overprotection_freq_t_init = IntegerField('Percent of time when', validators = [InputRequired()])    
    quiet_yes_t_init = BooleanField('Yes', validators = [Optional()])
    quiet_no_t_init = BooleanField('No', validators = [Optional()]) 

    # Comments
    treatments_spec_t_init = TextAreaField('Any other T specific treatments:', validators = [Optional()])
    problem_t = TextAreaField('Why is T a problem?', validators = [InputRequired()])   
    comments_t_init = TextAreaField('Comments:', validators = [Optional()])

    ''' SOUND TOLERANCE '''
    oversensitivity_yes_st = BooleanField('Yes', validators = [Optional()])
    oversensitivity_no_st = BooleanField('No', validators = [Optional()])
    physicaldisc_yes_st = BooleanField('Yes', validators = [Optional()])
    physicaldisc_no_st = BooleanField('No', validators = [Optional()])   
    description_sound_st = TextAreaField('Description of troublesome sound(s):', validators = [InputRequired()])

    # Activities prevented or affected
    concerts_st_init = BooleanField('Concerts', validators = [Optional()])
    shopping_st_init = BooleanField('Shopping', validators = [Optional()])
    movies_st_init = BooleanField('Movies', validators = [Optional()])
    work_st_init = BooleanField('Work', validators = [Optional()])
    restaurants_st_init = BooleanField('Restaurants', validators = [Optional()])
    driving_st_init = BooleanField('Driving', validators = [Optional()])
    sports_st_init = BooleanField('Sports', validators = [Optional()])
    church_st_init = BooleanField('Church', validators = [Optional()])
    housekeeping_st_init = BooleanField('Housekeeping', validators = [Optional()])
    childcare_st_init = BooleanField('Childcare', validators = [Optional()])
    social_st_init = BooleanField('Social', validators = [Optional()])
    other_st_init = BooleanField('Other', validators = [Optional()])

    # Severity, Annoyance, Effect on Life
    severity_st_init = IntegerField('Severity', validators = [InputRequired(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    annoyance_st_init = IntegerField('Annoyance', validators = [InputRequired(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    effectonlife_st_init = IntegerField('Effect on Life', validators = [InputRequired(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])

    # Bad Days 
    baddays_yes_st_init = BooleanField('Yes', validators = [Optional()])
    baddays_no_st_init = BooleanField('No', validators = [Optional()])
    baddays_freq_st_init = IntegerField('Frequency', validators = [InputRequired()])

    # Effect of Sound
    none_st_init = BooleanField('None', validators = [Optional()])
    louder_st_init = BooleanField('Louder', validators = [Optional()])
    softer_st_init = BooleanField('Softer', validators = [Optional()])
    mins_st_init = BooleanField('Mins', validators = [Optional()])
    hours_st_init = BooleanField('Hours', validators = [Optional()])
    days_st_init = BooleanField('Days', validators = [Optional()])

    # Ear overprotection
    overprotection_yes_st_init = BooleanField('Yes', validators = [Optional()])
    overprotection_no_st_init = BooleanField('No', validators = [Optional()])
    overprotection_freq_st_init = IntegerField('Percent of time when', validators = [InputRequired()])    
    quiet_yes_st_init = BooleanField('Yes', validators = [Optional()])
    quiet_no_st_init = BooleanField('No', validators = [Optional()]) 

    # Comments
    treatments_spec_st_init = TextAreaField('Any other ST specific treatments:', validators = [Optional()])
    problem_st = TextAreaField('Why is ST a problem?', validators = [InputRequired()])   
    comments_st_init = TextAreaField('Comments:', validators = [Optional()])

    '''HEARING'''
    problem_yes_hl = BooleanField('Yes', validators = [Optional()])
    problem_no_hl = BooleanField('No', validators = [Optional()])    
    aid_yes_hl = BooleanField('Yes', validators = [Optional()])
    aid_no_hl = BooleanField('No', validators = [Optional()])   
    aid_type_hl = StringField('Type:', validators = [Optional()])
    recommended_yes_hl = BooleanField('Yes', validators = [Optional()])
    recommended_no_hl_init = BooleanField('No', validators = [Optional()])     
    category_type_hl = StringField('Category:', validators = [InputRequired()])
    recommendation_type_hl = StringField('Recommendation:', validators = [InputRequired()])

    '''SUMMARY'''
    # Ranking problems
    tinnitus_init = IntegerField('Tinnitus', validators = [InputRequired(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    sound_tolerance_init = IntegerField('Sound Tolerance', validators = [InputRequired(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    hearing_init = IntegerField('Hearing', validators = [InputRequired(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    ptn_decision = StringField('Ptn Decision:', validators = [InputRequired()])
    next_visit_init = DateField('Next Visit:', validators = [InputRequired()])

    submit = SubmitField('Save', validators = [])
    comments_spec_t_init = StringField('Any other T specific treatments:', validators = [])
    problem_t_init = StringField('Why is T a problem?', validators = [])   
    
class AddFollowupInterviewForm(FlaskForm):
    # Beginning Info
    clinic_number = IntegerField('Clinic #:', validators = [])
    first_name = StringField('First Name:', validators = [])
    last_name = StringField('Last Name:', validators = [])
    dob = DateField('DOB:', validators = [])
    ssn = StringField('SSN:', validators = [])
    insurance = StringField('Insurance:', validators = [])
    date = DateField('Date:', validators = [])
    # followup own question
    category = StringField('GATEGORY: ', validators = [])
    date_of_init = DateField('Date of init. couns.: ', validators = [])
    date_of_instr = DateField('Date of instr. fitt.: ', validators = [])
    SG = StringField('SG: ', validators = [])
    HA = StringField('HA: ', validators = [])
    FUQ_num = StringField('FUQ #: ', validators = [])
    month = DateField('Month #:', validators = [])
    thc = IntegerField('T&HC:', validators = [])
    tel = StringField('tel: ', validators = [])

    # Tinn
# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField, SubmitField, DateField, BooleanField, TextAreaField, validators, DateField, validators
# from wtforms.validators import DataRequired, Required
# class AddVisitForm(FlaskForm):
#     visit_ID = IntegerField('Visit ID', validators=[DataRequired()])
#     patient_ID = IntegerField('Pateint Number',validators=[DataRequired()])
#     thc_number = IntegerField('TBH #',validators=[DataRequired()])
#     date = DateField('Date',validators=[DataRequired()], format = '%Y-%m-%d')
#     submit = SubmitField('Submit')


# class AddInterviewForm(FlaskForm):
#     visit_ID = StringField('Visit ID', validators = [])
#     date = DateField('Date', validators = [])
#     thc_number = IntegerField('THC #', validators = [])
#     patient_ID = StringField('Patient Number', validators = [])
#     visit_number = IntegerField('Visit No.', validators = [])

# class AddInitialInterviewForm(FlaskForm):
#     # Beginning info
#     clinic_number = IntegerField('Clinic #:', validators = [])
#     first_name = StringField('First Name:', validators = [])
#     last_name = StringField('Last Name:', validators = [])
#     dob = DateField('DOB:', validators = [])
#     ssn = IntegerField('SSN:', validators = [])
#     insurance = StringField('Insurance:', validators = [])
#     date = DateField('Date:', validators = [])
#     thc = IntegerField('T&HC:', validators = [])
#     telephone = IntegerField('Telephone:', validators = [])
#     email = StringField('Email:', validators = [])

#     ''' TINNITUTS '''
#     re = BooleanField('RE', validators = [])
#     le = BooleanField('LE', validators = [])
#     both = BooleanField('Both', validators = [])
#     head = BooleanField('Head', validators = [])
#     intermittent = BooleanField('Intermittent', validators = [])
#     constant = BooleanField('Constant', validators = [])

#     gradual = BooleanField('Gradual', validators = [])
#     sudden = BooleanField('Sudden', validators = [])
#     when = StringField('When', validators = [])
#     fluctuations_volume_yes = BooleanField('Yes', validators = [])
#     fluctuations_volume_no = BooleanField('No', validators = [])
#     description_t_sound = TextAreaField('Description of T sound(s):', validators = [])

#     # Activities prevented
#     concentration_t_init = BooleanField('Concentration', validators = [])
#     sleep_t_init = BooleanField('Sleep', validators = [])
#     qra_t_init = BooleanField('QRA', validators = [])
#     work_t_init = BooleanField('Work', validators = [])
#     restaurants_t_init = BooleanField('Restaurants', validators = [])
#     sports_t_init = BooleanField('Sports', validators = [])
#     social_t_init = BooleanField('Social', validators = [])
#     other_t_init = BooleanField('Other', validators = [])

#     # % of time when
#     aware_t_init = IntegerField('Aware', validators = [])
#     annoyed_t_init = IntegerField('Annoyed', validators = [])
#     severity_t_init = IntegerField('Severity', validators = [])
#     annoyance_t_init = IntegerField('Annoyance', validators = [])
#     effectonlife_t_init = IntegerField('Effect on Life', validators = [])

#     # Bad Days 
#     baddays_yes_t_init = BooleanField('Yes', validators = [])
#     baddays_no_t_init = BooleanField('No', validators = [])
#     baddays_freq_t_init = IntegerField('Frequency', validators = [])

#     # Effect of Sound
#     none_t_init = BooleanField('None', validators = [])
#     louder_t_init = BooleanField('Louder', validators = [])
#     softer_t_init = BooleanField('Softer', validators = [])
#     mins_t_init = BooleanField('Mins', validators = [])
#     hours_t_init = BooleanField('Hours', validators = [])
#     days_t_init = BooleanField('Days', validators = [])

#     # Ear overprotection
#     overprotection_yes_t_init = BooleanField('Yes', validators = [])
#     overprotection_no_t_init = BooleanField('No', validators = [])
#     overprotection_freq_t_init = IntegerField('Percent of time when', validators = [])    
#     quiet_yes_t_init = BooleanField('Yes', validators = [])
#     quiet_no_t_init = BooleanField('No', validators = []) 

#     # Comments
#     comments_spec_t_init = StringField('Any other T specific treatments:', validators = [])
#     problem_t_init = StringField('Why is T a problem?', validators = [])   
    
# class AddFollowupInterviewForm(FlaskForm):
#     #Beginning Info
#     clinic_number = IntegerField('Clinic #:', validators = [])
#     first_name = StringField('First Name:', validators = [])
#     last_name = StringField('Last Name:', validators = [])
#     dob = DateField('DOB:', validators = [])
#     ssn = IntegerField('SSN:', validators = [])
#     insurance = StringField('Insurance:', validators = [])
#     date = DateField('Date:', validators = [])
