# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import BooleanField, IntegerField, DecimalField, RadioField, StringField, TextAreaField, SelectField, FileField, PasswordField, HiddenField, SubmitField, validators # BooleanField

# Import Form validators
from wtforms.validators import Email, EqualTo, ValidationError

from app.main_page_module.models import User

#email verification
import re
import os.path

class LoginForm(FlaskForm):
    username_or_email = StringField('Username or Email', [validators.InputRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [validators.InputRequired(message='Must provide a password.')])
    remember = BooleanField()
    
    submit = SubmitField('Login')

class EditUserForm(FlaskForm):

    id = HiddenField('id', [validators.InputRequired(message='Dont fiddle around with the code!')])
    name   = StringField('Name', [validators.InputRequired(message='We need a name for the user.')])
    email    = StringField('Email', [validators.InputRequired(message='We need an email for your account.')])
    password  = PasswordField('Password')    
    password_2 = PasswordField('Repeat password', [EqualTo('password', message='Passwords must match')])
      
    submit = SubmitField('Submit changes')
    

class RegisterForm(FlaskForm):
    username   = StringField('Username', [validators.InputRequired(message='We need a username for your account.')])
    email    = StringField('Email', [validators.InputRequired(message='We need an email for your account.')])
    password  = PasswordField('Password')    
    password_2 = PasswordField('Repeat password', [validators.InputRequired(), EqualTo('password', message='Passwords must match')])
    
    submit = SubmitField('Register')
    
    #When you add any methods that match the pattern validate_<field_name>, WTForms takes those as custom validators and invokes them in addition to the stock validators
    def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')
    
    def validate_email(self, email):
        
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
        #check if it is a real email
        if(re.search(regex,email.data)):  
            #if it is, check if there is another user with the same email
            user = User.query.filter_by(email=email.data).first()
        
            if user is not None:
                raise ValidationError('Please use a different email address.')     
        
        else:  
            raise ValidationError('Please use a valid email address.')          
        
        
class LocationForm(FlaskForm):
    name          = StringField('Ime lokacije', [validators.InputRequired(message='We need the name of the location.')])
    description_s = StringField('Kratek opis', [validators.InputRequired(message='We need a short description.')])
    description_l = TextAreaField('Dolg opis', [validators.InputRequired(message='Write the long description.'),
                                               validators.Length(max=1300)])    
    
    categories = [(0, 'Uncategorised'), (1, 'History'), (2, 'Nature'), (3, 'Fun'), (4, 'Castle'), (5, 'Cave'), (6, 'Waterfall'), (7, 'Hilltop/Mountain')]
    category   = SelectField('Kategorija', [validators.InputRequired(message='Select a Category.')], choices=categories, coerce=int)
    
    photo_main = FileField(u'Glavna slika', [validators.regexp(u'^\[^/\\]\.(jpg|JPG|jpeg|JPEG|png|PNG)$'),
                                           validators.InputRequired(message='Select a Category.')])
    
    ratings  = [(0, 'If you have time, go see it once'), (1, 'Nothing special, but nice to see'), (2, 'Worth seeing if you can spare the time'), (3, 'Check it out, you wont regret it'), (4, 'Really good, top and see it'), (5, 'A must every time!')]
    rating   = SelectField('Ocena', [validators.InputRequired(message='Select a Rate.')], choices=ratings, coerce=int)
    
    tts      = IntegerField('Time To Spend', [validators.InputRequired(message='We need a username for your account.')])
    lat_l    = HiddenField('lat_l', [validators.InputRequired(message='We need a username for your account.')])
    lon_l    = HiddenField('lon_l', [validators.InputRequired(message='We need a username for your account.')])
    
    mtlds = [(0, 'PP0 - Easy, do not bother to mention'), (1, 'PP1 - Peacefull walk'), (2, 'PP2 - Can have some climbing protections'), (3, 'PP3 - Climbing protections, but not exposed, phisical strenght needed'), (4, 'PP4 - Vertical, exposed route'), (5, 'PP5 - Basicaly rock climbing with steel cables'), (6, 'PP6 - Like 5 but harder and more vertica')]
    mtld     = SelectField('Max To Location Difficulty', [validators.InputRequired(message='Select a Difficulty.')], choices=mtlds, coerce=int)
    
    webpage  = StringField('Spletna stran', [validators.InputRequired(message='We need a username for your account.')])
    telephone  = StringField('Telefon', [validators.InputRequired(message='We need a username for your account.')])
    email     = StringField('Elektronska pošta', [validators.InputRequired(message='We need a username for your account.')])
    
    timetable  = TextAreaField('Urnik', [validators.InputRequired(message='We need a username for your account.')])
    
    fees = [(0, 'Ne'), (1, 'Odvisno'), (2, 'Da')]
    fee  = SelectField('Vstopnina', [validators.InputRequired(message='Select if the location has fees.')], choices=fees, coerce=int)   
    
    childs = [(0, 'Ne'), (1, 'Odvisno'), (2, 'Da')]
    child  = SelectField('Primerno za otroke', [validators.InputRequired(message='Select if the location is suitable for children.')], choices=childs, coerce=int)   
    
    seasons = [(0, 'Ne'), (1, 'Da')]
    season  = SelectField('Letni čas pomemben', [validators.InputRequired(message='Select if the location is season dependant.')], choices=seasons, coerce=int)    
    
    submit = SubmitField('Submit')