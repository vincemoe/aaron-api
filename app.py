from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

quotes = ["You also have permission to tickle Tom now",
          "Well fudge",
          "Damn it, that's what I get for working in situ on VIM.  VPN dropped",]


class User(Resource):

    def get(self):
        quotetext = random.choice(quotes)
        if quotetext != "":
            return quotetext, 200
        else:
            return "Quote not found", 404


api.add_resource(User, "/quote")

app.run(debug=True, host='0.0.0.0')
