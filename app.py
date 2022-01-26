"""
        AUTHOR: GAUTAM CHANDRA SAHA
        DATE & TIME: 13/01/22 AT 5:09 PM ON Thu
"""

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import chat

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


port = 5050


def main():
    @app.route('/')
    def home():
        return jsonify({"home": "home for the ai chatbot"})

    @app.route('/message/<string:msg>', methods=['POST'])
    def post(msg):
        if(msg[0] == "?"):
            return jsonify(
                {'message': "Sorry, did not understand!"}
            )
        response = chat.main(msg)

        print(f"{response}: to {msg}")
        return jsonify(
            {'message': response}
        )

    app.run(port=port)


if __name__ == "__main__":
    main()
