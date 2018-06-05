from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

quotes = ["'You also have permission to tickle Tom now' - Aaron B",
          "'Well fudge' - Aaron B",
          "'Damn it, that's what I get for working in situ on VIM.  VPN dropped' - Aaron B",
          "'Yeah, turns out, I'm just a horse's a**' - Aaron B",
          "'Who...am I?' - Aaron B",
          "'Ha, Oh, I'm always watching' - Aaron B",
          "'I bet if we summoned Linus Torvalds, first, we notice what a f*cking weird dude he is' - Aaron B",
          "'I will slap someone if you don't get a UAT response by end of day' - Aaron B",
          "'Haha, damn it. GET OUT OF MY HEAD!!!' - Aaron B",
          "'I have a spreadsheet titled 'PB Bureaucracy Navigation'' - Aaron B",
          "'Well, Gabby just got up, walked across the living room (the big event)....and slapped the dog' - Aaron B",
          "'Just saw a dude with a giant juggalo tattoo biking next to his friend with a duster and matrix glasses going by...my day might need to end' - Aaron B",
          "'If I type 'cocker'....one more time' - Aaron B",
          "'As a capitalist merc with proletariat tendencies, I endorse this private room' - Aaron B",
          "'Don't start projects you don't plan on finishing (Or Something Like That)' - Aaron B",
          "'If we hire another midwesterner, I'll show up, scream 'There can be only ONE!' and disembowel said individual.' - Aaron B",
          "'David Letterman, he went to my high school.' - Aaron B",
          "'Don't Google that if you're unsure.' - Aaron B",
          "'I've always enjoyed this article (no relation).' - Aaron B",
          "'You're such a Cathy.' - Aaron B"
          ]


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
