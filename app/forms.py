from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, validators
from wtforms.validators import DataRequired, InputRequired, NumberRange, Email, Optional
from wtforms import StringField, IntegerField, DateField, BooleanField, TextAreaField, validators
from wtforms.validators import DataRequired, Required



class AddVisitForm(FlaskForm):
    """
    form that is used in /add_visit page

    Each variable is set to a field in the form
    and validators are specified in the argument
    """
    visit_ID = IntegerField('Visit ID', validators=[DataRequired()])
    # patient_ID = IntegerField('Pateint Number',validators=[DataRequired()])
    thc_number = IntegerField('TBH #',validators=[DataRequired()])
    # date = DateField('Date',validators=[DataRequired()], format = '%Y-%m-%d')
    date = StringField('Date',validators=[DataRequired()])
    visit_num = IntegerField('Visit Numer',validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddInterviewForm(FlaskForm):
    visit_ID = StringField('Visit ID', validators = [Optional()])
    date = DateField('Date', validators = [Optional()])
    thc_number = IntegerField('THC #', validators = [Optional()])
    patient_name = StringField('Patient Name', validators = [Optional()])
    visit_number = IntegerField('Visit No.', validators = [Optional()])

class AddInitialInterviewForm(FlaskForm):
    # Beginning info
    clinic_number = IntegerField('Clinic #:', validators = [Optional()])
    first_name = StringField('First Name:', validators = [Optional()])
    last_name = StringField('Last Name:', validators = [Optional()])
    dob = DateField('DOB:', validators = [Optional()])
    ssn = IntegerField('SSN:', validators = [Optional(), NumberRange(min = 000000000, max = 999999999, message = "SSN must be 9 digits")])
    insurance = StringField('Insurance:', validators = [Optional()])
    date = DateField('Date:', validators = [Optional()])
    thc = IntegerField('T&HC:', validators = [Optional()])
    telephone = IntegerField('Telephone:', validators = [Optional(), NumberRange(min = 0000000000, max = 9999999999, message = "Telephone number must be 10 digits")])
    email = StringField('Email:', validators = [Optional(), Email()])

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
    description_t_sound = TextAreaField('Description of T sound(s):', validators = [Optional()])

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
    aware_t_init = IntegerField('Aware', validators = [Optional(), NumberRange(min = 0, max = 100, message = "Number must be between 0 and 100")])
    annoyed_t_init = IntegerField('Annoyed', validators = [Optional(), NumberRange(min = 0, max = 100, message = "Number must be between 0 and 100")])
    severity_t_init = IntegerField('Severity', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 100")])
    annoyance_t_init = IntegerField('Annoyance', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    effectonlife_t_init = IntegerField('Effect on Life', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])

    # Bad Days 
    baddays_yes_t_init = BooleanField('Yes', validators = [Optional()])
    baddays_no_t_init = BooleanField('No', validators = [Optional()])
    baddays_freq_t_init = IntegerField('Frequency', validators = [Optional()])

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
    overprotection_freq_t_init = IntegerField('Percent of time when', validators = [Optional()])    
    quiet_yes_t_init = BooleanField('Yes', validators = [Optional()])
    quiet_no_t_init = BooleanField('No', validators = [Optional()]) 

    # Comments
    treatments_spec_t_init = TextAreaField('Any other T specific treatments:', validators = [Optional()])
    problem_t = TextAreaField('Why is T a problem?', validators = [Optional()])   
    comments_t_init = TextAreaField('Comments:', validators = [Optional()])

    ''' SOUND TOLERANCE '''
    oversensitivity_yes_st = BooleanField('Yes', validators = [Optional()])
    oversensitivity_no_st = BooleanField('No', validators = [Optional()])
    physicaldisc_yes_st = BooleanField('Yes', validators = [Optional()])
    physicaldisc_no_st = BooleanField('No', validators = [Optional()])   
    description_sound_st = TextAreaField('Description of troublesome sound(s):', validators = [Optional()])

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
    severity_st_init = IntegerField('Severity', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    annoyance_st_init = IntegerField('Annoyance', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    effectonlife_st_init = IntegerField('Effect on Life', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])

    # Bad Days 
    baddays_yes_st_init = BooleanField('Yes', validators = [Optional()])
    baddays_no_st_init = BooleanField('No', validators = [Optional()])
    baddays_freq_st_init = IntegerField('Frequency', validators = [Optional()])

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
    overprotection_freq_st_init = IntegerField('Percent of time when', validators = [Optional()])    
    quiet_yes_st_init = BooleanField('Yes', validators = [Optional()])
    quiet_no_st_init = BooleanField('No', validators = [Optional()]) 

    # Comments
    treatments_spec_st_init = TextAreaField('Any other ST specific treatments:', validators = [Optional()])
    problem_st = TextAreaField('Why is ST a problem?', validators = [Optional()])   
    comments_st_init = TextAreaField('Comments:', validators = [Optional()])

    '''HEARING'''
    problem_yes_hl = BooleanField('Yes', validators = [Optional()])
    problem_no_hl = BooleanField('No', validators = [Optional()])    
    aid_yes_hl = BooleanField('Yes', validators = [Optional()])
    aid_no_hl = BooleanField('No', validators = [Optional()])   
    aid_type_hl = StringField('Type:', validators = [Optional()])
    recommended_yes_hl = BooleanField('Yes', validators = [Optional()])
    recommended_no_hl_init = BooleanField('No', validators = [Optional()])     
    category_type_hl = StringField('Category:', validators = [Optional()])
    recommendation_type_hl = StringField('Recommendation:', validators = [Optional()])

    '''SUMMARY'''
    # Ranking problems
    tinnitus_init = IntegerField('Tinnitus', validators = [Optional(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    sound_tolerance_init = IntegerField('Sound Tolerance', validators = [Optional(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    hearing_init = IntegerField('Hearing', validators = [Optional(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    ptn_decision = StringField('Ptn Decision:', validators = [Optional()])
    next_visit_init = DateField('Next Visit:', validators = [Optional()])

    submit = SubmitField('Save', validators = [Optional()])
    comments_spec_t_init = StringField('Any other T specific treatments:', validators = [Optional()])
    problem_t_init = StringField('Why is T a problem?', validators = [Optional()])   
    
class AddFollowupInterviewForm(FlaskForm):
    # Beginning Info
    clinic_number = IntegerField('Clinic #:', validators = [Optional()])
    first_name = StringField('First Name:', validators = [Optional()])
    last_name = StringField('Last Name:', validators = [Optional()])
    dob = DateField('DOB:', validators = [Optional()])
    ssn = StringField('SSN:', validators = [Optional()])
    insurance = StringField('Insurance:', validators = [Optional()])
    date = DateField('Date:', validators = [Optional()])
    # followup own question
    category = StringField('Gategory: ', validators = [Optional()])
    date_of_init = DateField('Date of init. couns.: ', validators = [Optional()])
    date_of_instr = DateField('Date of instr. fitt.: ', validators = [Optional()])
    SG = StringField('SG: ', validators = [Optional()])
    HA = StringField('HA: ', validators = [Optional()])
    FUQ_num = StringField('FUQ #: ', validators = [Optional()])
    month = DateField('Month #:', validators = [Optional()])
    thc = IntegerField('T&HC:', validators = [Optional()])
    tel = StringField('tel: ', validators = [Optional()])

    # Tinn
    
    # Activities prevented or affected
    concentration_t_init = BooleanField('Concentration', validators = [Optional()])
    sleep_t_init = BooleanField('Sleep', validators = [Optional()])
    qra_t_init = BooleanField('QRA', validators = [Optional()])
    work_t_init = BooleanField('Work', validators = [Optional()])
    restaurants_t_init = BooleanField('Restaurants', validators = [Optional()])
    sports_t_init = BooleanField('Sports', validators = [Optional()])
    social_t_init = BooleanField('Social', validators = [Optional()])
    other_t_init = BooleanField('Other', validators = [Optional()])
    
    # percent_time_when_aware and annoyed
    aware_t_init = IntegerField('Aware(1st)', validators = [Optional(), NumberRange(min = 0, max = 100, message = "Number must be between 0 and 100")])
    annoyed_t_init = IntegerField('Annoyed(1st)', validators = [Optional(), NumberRange(min = 0, max = 100, message = "Number must be between 0 and 100")])
    severity_t_init = IntegerField('Severity (1-10)', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    annoyance_t_init = IntegerField('Annoyance (1-10)', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])
    effectonlife_t_init = IntegerField('Effect on Life (1-10)', validators = [Optional(), NumberRange(min = 0, max = 10, message = "Number must be between 0 and 10")])

    # Bad Days 
    baddays_yes_t_init = BooleanField('Yes', validators = [Optional()])
    baddays_no_t_init = BooleanField('No', validators = [Optional()])
    baddays_freq_t_init = IntegerField('Frequency', validators = [Optional()])  

    # are frequent
    areFrequent_yes_t_init = BooleanField('Yes', validators = [Optional()])
    areFrequent_no_t_init = BooleanField('No', validators = [Optional()])
    areBad_yes_t_init = BooleanField('Yes', validators = [Optional()])
    areBad_no_t_init = BooleanField('No', validators = [Optional()])

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
    overprotection_freq_t_init = IntegerField('Percent of time when', validators = [Optional()])    
    quiet_yes_t_init = BooleanField('Yes', validators = [Optional()])
    quiet_no_t_init = BooleanField('No', validators = [Optional()]) 

    # Comments
    treatments_spec_t_init = TextAreaField('Any other T specific treatments:', validators = [Optional()])
    comments_t_init = TextAreaField('Comments:', validators = [Optional()])

    #Hearing
    PinG_Same = BooleanField('Same ', validators = [Optional()])
    PinG_Better = BooleanField('Better ', validators = [Optional()])
    PinG_Worse = BooleanField('Worse ', validators = [Optional()])
    tinnitus_init = IntegerField('Tinnitus', validators = [Optional(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    sound_tolerance_init = IntegerField('Sound Tolerance', validators = [Optional(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    hearing_init = IntegerField('Hearing', validators = [Optional(), NumberRange(min = 0, max = 5, message = "Number must be between 0 and 5")])
    feedback_yes = BooleanField(' Yes', validators = [Optional()])
    feedback_no = BooleanField(' No', validators = [Optional()])
    feedback_ns = BooleanField(' NS', validators = [Optional()])

    mp_discussed = TextAreaField('Main problems discussed:', validators = [Optional()])
