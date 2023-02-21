from flask_cors import *
from flask_httpauth import HTTPBasicAuth
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import openai
import os

openai.api_key = os.environ['openai.api_key']

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
CORS(app, supports_credentials=True)

users = [
    {'username': 'chatgpt', 'password': 'chatgpt'},
]

model_engine = "text-davinci-003"


class Prompt(Resource):
    def put(self):
        prompt = request.form['text']
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return jsonify(response)


api.add_resource(Prompt, '/prompt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
