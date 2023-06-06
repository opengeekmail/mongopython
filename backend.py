from flask import Flask, redirect, url_for,session,request ,jsonify,json

#from secret import secret_key
from flask_pymongo import PyMongo
from flask_cors import CORS
from datetime import datetime
from bson import json_util

app = Flask(__name__)
CORS(app)

#app.config['SECRET_KEY'] = secret_key #'your-secret-key'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/mydb'  ## Mongo db connection
mongo = PyMongo(app)


# API endpoint for storing search history
@app.route('/registration', methods=['POST'])
def registration():
    data = request.json
    user_id = data['user_id']
    mobilenumber = data['mobilenumber']
    timestamp = datetime.now()

    # Store the registrants details in MongoDB
    mongo.db.users.insert_one({
        'user_id': user_id,
        'mobilenumber': mobilenumber,
        'timestamp': timestamp
    })

    return {'message': 'Registrants details stored successfully'}

# API endpoint for retrieving search history
@app.route('/report/<user_id>', methods=['GET'])
def get_report(user_id):
    try:
        user_id = user_id
        # Retrieve search history from the database
        user_details = mongo.db.users.find({'user_id': user_id})

        user_details_list = []
        for doc in user_details:
             serialized_doc = {
            # '_id': str(doc['_id']),
            'user_id': doc['user_id'],
            'mobilenumber': doc['mobilenumber'],
            # 'timestamp': doc['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        }
        user_details_list.append(serialized_doc)

        # Convert the user details list to JSON using jsonify
        return jsonify({'search_history': user_details_list})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
