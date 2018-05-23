from flask import Flask

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost:5432/test_travis_2'

# db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
