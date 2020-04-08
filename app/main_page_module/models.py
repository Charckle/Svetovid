# Import the database object (db) from the main application module
from app import db

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'users_table'

    # User Name
    name    = db.Column(db.String(128),  nullable=False)
    
    # UserName
    username    = db.Column(db.String(128),  nullable=False,
                            unique=True)    

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                         unique=True)
    password = db.Column(db.String(192),  nullable=False)

    # Authorisation Data: role & status
    role     = db.Column(db.SmallInteger, nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)
    

    # New instance instantiation procedure
    def __init__(self, username, email, password):

        self.name     = username
        self.username = username
        self.email    = email
        self.password = password
        self.role = 0
        self.status = 1

    def __repr__(self):
        return '<User %r>' % (self.name)
    
    def set_password(self, password):
            self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password) 

class Location(Base):

    __tablename__ = 'users_table'
    
    # Creator ID
    creator_id  = db.Column(db.Integer(7),  nullable=False)    
    # Name
    name  = db.Column(db.String(128),  nullable=False)
    # short description
    description_s = db.Column(db.String(128),  nullable=False)
    # long description
    description_l = db.Column(db.String(1300),  nullable=False)  
    # Main Photo
    photo_main  = db.Column(db.String(128),  nullable=False)    
    # Category
    category = db.Column(db.Integer(3),  nullable=False)
    # Rating
    rating = db.Column(db.Integer(2),  nullable=False)
    # Time To Spend
    tts = db.Column(db.Integer(4),  nullable=False)
    # latitude of location
    lat_l = db.Column(db.Long(20),  nullable=False)
    # longitude of location
    lon_l = db.Column(db.Long(20),  nullable=False)
    # latitude of start
    lat_l_s = db.Column(db.Long(20),  nullable=False)
    # longitude of start
    lon_l_s = db.Column(db.Long(20),  nullable=False)
    # Maximum to location difficulty
    mtld = db.Column(db.Integer(2),  nullable=False)
    
    # webpage
    webpage  = db.Column(db.String(128),  nullable=False)    
    # telephone
    telephone  = db.Column(db.String(128),  nullable=False)
    # email
    email  = db.Column(db.String(128),  nullable=False)
    
    # timetable
    timetable  = db.Column(db.String(128),  nullable=False)
    # fee
    fee = db.Column(db.Integer(1),  nullable=False)
    # children suitable
    child = db.Column(db.Integer(1),  nullable=False)
    # season dependant
    season = db.Column(db.Integer(1),  nullable=False)
    
    # verified - team checked out the location
    verified = db.Column(db.Integer(1),  nullable=False)
    # displayed - is the location displayed in the webpage
    displayed = db.Column(db.Integer(1),  nullable=False)
    # suggestion
    suggestion = db.Column(db.Integer(1),  nullable=False)
    
    # New instance instantiation procedure
    def __init__(self, creator_id, name, description_s, description_l, category, rating, tts, lat_l, lon_l, lat_l_s, lon_l_s, mtld, webpage, telephone, email, timetable, fee, child, season):

        self.creator_id    = creator_id
        self.name          = name
        self.description_s = description_s
        self.description_l = description_l
        self.category      = category
        self.photo_main    = photo_main
                
        self.rating  = rating
        self.tts     = tts
        self.lat_l   = lat_l
        self.lon_l   = lon_l  
        self.lat_l_s = lat_l_s
        self.lon_l_s = lon_l_s
        self.mtld    = mtld
        
        self.webpage  = webpage
        self.telephone = telephone
        self.email = email
        
        self.timetable = timetable   
        self.fee       = fee
        self.child     = child
        self.season    = season        
        
        self.verified = 0
        self.displayed = 0
        self.suggestion = 1

    def __repr__(self):
        return '<Location %r>' % (self.name)    