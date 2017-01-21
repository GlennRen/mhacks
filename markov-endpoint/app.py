import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# parser.add_argument('message')

class Messages(Resource):
    def get(self):
    	# https://github.com/jsvine/markovify
    	import markovify

        messages = {
            "messages": []
        }
    	# Get raw text as string.
    	with open("../Facebook Data/messages.txt") as f:
    	    text = f.read()


    	# Build the model.
        # for i in range(10):
        text_model = markovify.Text(text)
            # messages["messages"].append({'message': text_model.make_sentence().capitalize()})
    	# Print five randomly-generated sentences
        return {'message': text_model.make_sentence().capitalize()}

api.add_resource(Messages, '/message')

if __name__ == '__main__':
    app.run(debug=True)
