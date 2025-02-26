from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask App Deployed on Netlify!"})

# Required for Netlify function handler
def handler(event, context):
    from flask_lambda import make_lambda_function
    return make_lambda_function(app)(event, context)
