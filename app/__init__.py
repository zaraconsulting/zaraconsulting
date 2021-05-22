from flask import Flask
from config import Config
from logging.handlers import SMTPHandler, RotatingFileHandler
import os, logging
from flask_mail import Mail

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)

    with app.app_context():
        from .import routes, models, context_processors

    # Email Error Logging
    # if not app.debug:
    #     server = app.config.get('MAIL_SERVER')
    #     username = app.config.get('MAIL_USERNAME')
    #     port = app.config.get('MAIL_PORT')
    #     password = app.config.get('MAIL_PASSWORD')
    #     use_tls = app.config.get('MAIL_USE_TLS')
    #     admin = app.config.get('ADMIN')

    #     if server:
    #         auth = None
    #         if username or password:
    #             auth = (username, password)
    #         secure = None
    #         if use_tls:
    #             secure = ()
    #         mail_handler = SMTPHandler(
    #             mailhost=(server, port),
    #             fromaddr=f'noreply@{server}',
    #             toaddrs=admin,
    #             subject='Zara Consulting Failure',
    #             credentials=auth,
    #             secure=secure
    #         )
    #         mail_handler.setLevel(logging.ERROR)
    #         app.logger.addHandler(mail_handler)
    #     if not os.path.exists('logs'):
    #         os.mkdir('logs')
    #     file_handler = RotatingFileHandler(
    #         'logs/zaraconsulting-message_handlers.log',
    #         maxBytes=10240,
    #         backupCount=10
    #     )
    #     file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s [%(pathname)s:%(lineno)d]"))
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)
    #     app.logger.setLevel(logging.INFO)
    #     app.logger.info('Zara Consulting startup')

    return app