# from flask import Flask
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello ChuChu.'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'chuchu'}

if __name__ == '__main__':
    app.run(debug=True)
