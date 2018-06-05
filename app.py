from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

quotes = ["You also have permission to tickle Tom now",
          "Well fudge",
          "Damn it, that's what I get for working in situ on VIM.  VPN dropped",
          "Yeah, turns out, I'm just a horse's a**",
          "Who...am I?",
          "Ha, Oh, I'm always watching",
          "I bet if we summoned Linus Torvalds, first, we notice what a f*cking weird dude he is",
          "I will slap someone if you don't get a UAT response by end of day",
          "Haha, damn it. GET OUT OF MY HEAD!!!",
          "I have a spreadsheet titled 'PB Bureaucracy Navigation'",
          "Well, Gabby just got up, walked across the living room (the big event)....and slapped the dog",
          "Just saw a dude with a giant juggalo tattoo biking next to his friend with a duster and matrix glasses going by...my day might need to end",
          "If I type 'cocker'....one more time",
          "As a capitalist merc with proletariat tendencies, I endorse this private room",
          "Don't start projects you don't plan on finishing (Or Something Like That)",]


class User(Resource):

    def get(self):
        quotetext = random.choice(quotes)
        if quotetext != "":
            return {
                       "response_type": "in_channel",
                       "text": quotetext,
                   }, 200
        else:
            return "Quote not found", 404


api.add_resource(User, "/quote")

app.run(debug=True, host='0.0.0.0')
