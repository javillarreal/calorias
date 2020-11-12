from flask import Flask, flash, render_template, request, jsonify, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from six.moves.urllib.parse import urlencode
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_cors import CORS

from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from base64 import encodebytes
from PIL import Image
from config import Config
import settings
from image_functions import *


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_object(Config)
app.debug = Config.DEBUG

#Set up database
db = SQLAlchemy(app)

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

from models import *

#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/create-food', methods=['POST'])
def create_food():
    try:
        name = request.json.get('name', None)
        calories = request.json.get('calories', None)
        weight = request.json.get('weight', None)

        if not name:
            return 'Missing name', 400
        if not calories:
            return 'Missing calories', 400
        if not weight:
            return 'Missing weight', 400

        food = Food(name=name, calories=calories, weight=weight)
        db.session.add(food)
        db.session.commit()

        #access_token = create_access_token(identity={"email": email})
        return "Food has been created", 200
    except IntegrityError:
        # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return 'Food Already Exists', 400
    except AttributeError:
        return 'Provide name, calories and weight in JSON format in the request body', 400

@app.route('/register', methods=['POST'])
def register():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400

        user = User(email=email, password_hash=password)
        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity={"email": email})
        return {"access_token": access_token}, 200
    except IntegrityError:
        # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return 'User Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/user/<int:id>')
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return "No user with that ID"

    return jsonify({"user": user.email}), 200

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if request.method == "DELETE":
        user = User.query.filter_by(id=id).first()
        if not user:
            return "No user with that ID"

        db.session.delete(user)
        db.session.commit()

    return "User has been deleted", 200

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"msg": "User not found"}), 404

    if not user.check_password(password):
        return jsonify({"msg": "Password from PIL import Imageincorrect"}), 401

    access_token = create_access_token(identity={"email": email})
    return jsonify(access_token=access_token), 200


# protected test route
@app.route('/test', methods=['GET'])
@jwt_required
def test():
    user = get_jwt_identity()
    email = user['email']
    return f'Welcome to the protected route {email}!', 200

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if 'image' not in request.files:
            flash('No file part')
            return "No pic uploaded", 400
        image = request.files['image']
        if image.filename == '':
            flash('No selected file')
            return "No selected file", 400
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            [filename,num] = filename.split(".")
            image = crop_images(app.config['IMAGE_UPLOADS'], image, 224, 224, 0, 1, 0, filename)
            if image != True:
                return "Image needs to be 960x960 or higher", 400

            result = get_images(app.config['IMAGE_UPLOADS'])
            #print(result)
            return jsonify({'result': result})
            #return result
            #result = convert_to_numpy(app.config['IMAGE_UPLOADS'])
            #return jsonify({"msg": "Image has been cropped"}), 200

@app.route("/load-images", methods=["GET", "POST"])
def load_images():
    if request.method == "POST":
        #receives array of strings
        data = request.form.getlist("image")[0].split(",")
        print("data:", data)
        #make prediction
        result = make_prediction(data,app.config['IMAGE_UPLOADS'])
        return jsonify({'result': result})
        #retornar json con


@app.route("/calories-estimation", methods=["GET", "POST"])
def calories_estimation():
    if request.method == "POST":
        food = request.form.getlist("check")[0].split(",")
        #print(food)
        total_calories = 0
        for f in food:
            food = Food.query.filter_by(name=f).first()
            total_calories = total_calories + food.calories

        return jsonify({'result': total_calories})


if __name__ == '__main__':
    app.run()
