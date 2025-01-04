from flask import Flask, render_template,request,session,redirect,url_for
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB Configuration
MONGO_URI = "mongodb+srv://krishnareddy:1234567890@diploma.1v5g6.mongodb.net/"
DB_NAME = "banking"

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users=db['users']
transactions=db['transactions']

@app.route("/")
def index():
    return "server is running"

@app.route("/checkbal", methods=['POST'])
def checkbal():
    id = request.args.get('id')
    
    # Find the user in the MongoDB collection
    user = users.find_one({"customerid": id})
    
    if not user:
        return jsonify({"error": "User does not exist"}), 404  # Return a 404 error if user doesn't exist
    
    # Return the user's balance as a JSON response
    return jsonify({"customerid": id, "balance": user.get('balance')}), 200  

if __name__ == '__main__':
    app.run(debug=True)
