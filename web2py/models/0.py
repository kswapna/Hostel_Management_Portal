from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'My New App'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '55764467-f45e-42f0-92fd-28d76d9e21f8'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
