from flask import request, jsonify
from config import app, db
from models import Contact

# GET method
@app.route("/contacts", methods = ["GET"])
def get_connacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

# CREAT method
@app.route("/create_contacts", methods = ["POST"])
def create_connacts():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You have to have the infor"}),
            400,
        )
    new_contact = Contact(first_name=first_name,last_name = last_name, email = email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

# Update method
@app.route("/update_contact/<int:user_ud>", methods = ["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "User not found"}),404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    db.session.commit()
    
    return jsonify({"message": "User Updated"}), 200


# Delet method
@app.route("/delete_contacts<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "User not found"}),404
    
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({"message": "User delete"}),200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)
    