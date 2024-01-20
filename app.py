from flask import Flask, jsonify,request

app = Flask(__name__)

# Sample data for testing Flask API
users_data = [
    {'id': 1, 'username': 'john_doe', 'email': 'john@example.com', 'age': 28},
    {'id': 2, 'username': 'alice_smith', 'email': 'alice@example.com', 'age': 24},
    {'id': 3, 'username': 'bob_jones', 'email': 'bob@example.com', 'age': 32},
    # Add more entries as needed
]

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users_data)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users_data:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'message': 'No result found'}), 404

@app.route('/insert_user/',methods=['POST'])
def pusers():
    user={'id':len(users_data)+1,'username':request.json['username'],'email':request.json['email'],'age':request.json['age']}
    users_data.append(user)
    return user

@app.route('/put_users/<int:user_id>',methods=['PUT'])
def puusers(user_id):
    for user in users_data:
        if user['id']==user_id:
            user['user_name']=request.json['user_name']
            user['email']=request.json['email']
            user['age']=request.json['age']
            return user
@app.route('/delete_user/<int:user_id>',methods=['DELETE'])
def delusers(user_id):
    for user in user_id:
        if user['user_id']==user_id:
            users_data.remove(user)
       




if __name__ == '__main__':
    app.run(debug=True)


