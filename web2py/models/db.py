# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables

########################################
db.define_table('auth_user',
    Field('username', type='string',
          label=T('Username')),
    Field('first_name', type='string',
          label=T('First Name')),
    Field('last_name', type='string',
          label=T('Last Name')),
    Field('email', type='string',
          label=T('Email')),
    Field('password', type='password',
          readable=False,
          label=T('Password')),
    Field('created_on','datetime',default=request.now,
          label=T('Created On'),writable=False,readable=False),
    Field('modified_on','datetime',default=request.now,
          label=T('Modified On'),writable=False,readable=False,
          update=request.now),
    Field('registration_key',default='',
          writable=False,readable=False),
    Field('reset_password_key',default='',
          writable=False,readable=False),
    Field('registration_id',default='',
          writable=False,readable=False),
    format='%(username)s',
    migrate=settings.migrate)


db.auth_user.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.password.requires = CRYPT(key=auth.settings.hmac_key)
db.auth_user.username.requires = IS_NOT_IN_DB(db, db.auth_user.username)
db.auth_user.email.requires = (IS_EMAIL(error_message=auth.messages.invalid_email),
                               IS_NOT_IN_DB(db, db.auth_user.email))
auth.define_tables(migrate = settings.migrate)

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login

db.define_table('complaint',  
   Field('User',writable=False,readable=False),
   Field('access',requires=IS_IN_SET(['Public','Private'])),
   Field('category',requires=IS_IN_SET(['Carpenter','Plumber','Electrician','Other'])),
   Field('complaint_body', 'text'),
   Field('Date','date',writable=False,readable=False),
   Field('Time','time',writable=False,readable=False),
   Field('Flag','integer',writable=False,readable=False),
   Field('AvailableTime','time',label=T('Available time(HH:MM:SS)'),default="16:00:00"),
   Field('room',writable=False,readable=False)
)
db.define_table('students',
    Field('name'),
    Field('roll_no'),
    Field('room_no'),
    Field('email'),
    Field('blood_grp'),
    Field('hostel'),
    Field('file','upload'),
    Field('branch','string'),
    Field('mobile','integer')
    )
    
db.define_table('admin',
    Field('email'))
    
db.define_table('puser',
    Field('email'))
    
db.define_table('nuser',
    Field('email'))    
  
db.define_table('staff',
    Field('email'))  
            
db.define_table('laptop',
Field('roll_no'),
Field('company',requires=IS_IN_SET(["ACER","APPLE","Asus","COMPAQ","DELL","HP","IBM","LENOVO","SAMSUNG","SONY","TOSHIBHA","other"],zero=None)),
Field('service_tag'))

db.define_table('laptop_out',
Field('roll_no'),
Field('out_time','datetime',default=request.now,writable=False,readable=False),
Field('reason',requires=IS_IN_SET(["Library","Openlab","Class","outside campus"],zero=None))
)

db.define_table('other_laptop_out',
Field('roll_no'),
Field('out_time','datetime',default=request.now,writable=False,readable=False),
Field('reason',requires=IS_IN_SET(["Library","Openlab","Class","outside campus"],zero=None)),
Field('laptop_company',requires=IS_IN_SET(["ACER","APPLE","Asus","COMPAQ","DELL","HP","IBM","LENOVO","SAMSUNG","SONY","TOSHIBHA","other"],zero=None)),
Field('laptop_service_tag'))



db.define_table('student_out',
Field('roll_no'),
Field('out_time','datetime',default=request.now,writable=False,readable=False),
Field('reason',requires=IS_IN_SET(["Holidays","sick","Others"],zero=None)),Field('laptop_presence',requires=IS_IN_SET(["present","NotPresent "],zero=None)))

db.define_table('news_feed',
Field('flag','integer',readable=False,writable=False),
Field('Title'),
Field('posted_by',readable=False,writable=False),
Field('image','upload'),
Field('description','text'))


db.define_table('medical',
Field('posted_by',readable=False,writable=False),
Field('Doctor',requires=IS_IN_SET(["Homiopathi","Allopathi","Ayurvedhic","Others"],zero=None)),
Field('mobile','integer'),
Field('Date','date',writable=False,readable=False),
Field('Time','time',writable=False,readable=False),
Field('Flag','integer',writable=False,readable=False)
)

db.define_table('poll',
Field('flag','integer',readable=False,writable=False),

Field('posted_by',readable=False,writable=False),
Field('question'),
Field('options_no','integer',readable=False,writable=False),
Field('counter','integer',readable=False,writable=False))

db.poll.counter.default=0

db.define_table('options',
Field('option'),
Field('qid'),
Field('counter','integer'))
db.options.counter.default=0

db.define_table('vote',
Field('voted_by','string'),
Field('qid','integer'))

db.define_table('vacant_rooms',
Field('hostel'),
Field('room_no'),
Field('date','datetime',default=request.now,writable=False,readable=False))

db.define_table('features',
Field('feature'),
Field('status','boolean'),
Field('request_newsfeed','boolean'),
Field('request_poll','boolean'),
Field('request_vacant_rooms','boolean'),
Field('request_edit_profile','boolean'),
Field('display_vacant_rooms','boolean'),
Field('display_guestrooms','boolean'),
Field('request_guestrooms','boolean'),
Field('complaint_completed_to_user','boolean'),
Field('complaint_completed_to_staff','boolean'),
)


db.define_table('rules',
Field('rule','text')
)

db.define_table('docs',
Field('Doctor_Name'),
Field('Phone_No'),
Field('category',requires=IS_IN_SET(["Homiopathi","Allopathi","Ayurvedhic","Others"],zero=None)),

Field('Available_day_and_time')
)
