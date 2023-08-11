from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    birth_date = db.Column(db.String(20))

# db.create_all()

@app.route('/api/users', methods=['GET'])
def get_users():
    first_name = request.args.get('first_name')

    if not first_name:
        return jsonify(message='Missing mandatory parameter: first_name'), 400

    matching_users = User.query.filter(User.first_name.startswith(first_name)).all()

    if matching_users:
        result = [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
                'gender': user.gender,
                'email': user.email,
                'phone': user.phone,
                'birth_date': user.birth_date
            }
            for user in matching_users
        ]
        return jsonify(result)
    else:
        # Fetch from the external API and save to the database
        import requests
        response = requests.get(f'https://dummyjson.com/users/search?q={first_name}')
        new_users = response.json()

        for user_data in new_users:
            new_user = User(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                age=user_data['age'],
                gender=user_data['gender'],
                email=user_data['email'],
                phone=user_data['phone'],
                birth_date=user_data['birth_date']
            )
            db.session.add(new_user)
        db.session.commit()

        return jsonify(new_users)

if __name__ == '__main__':
    app.run(debug=True)
