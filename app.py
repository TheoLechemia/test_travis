from flask import Flask


def get_app():
    app = Flask(__name__)
    from .blueprint import api
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost:5432/test_travis_2'
    # db = SQLAlchemy(app)
    app.register_blueprint(api, url_prefix='/api')
    return app
    


if __name__ == '__main__':
    get_app().run()
