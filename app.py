from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import os
from quotes import quotes as q

app = Flask(__name__)
api = Api(app)


class User(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token")
        args = parser.parse_args()

        quotetext = random.choice(q)
        if quotetext != "" and os.environ['TOKEN'] == args["token"]:
            return {
                       "response_type": "in_channel",
                       "text": "'" + quotetext + "' - Aaron B",
                   }, 200
        else:
            return "Wrong Token", 404


api.add_resource(User, "/quote")

app.run(debug=True, host='0.0.0.0')
