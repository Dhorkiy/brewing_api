from flask import Flask, request, jsonify
#from flask.ext.sqlalchemy import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bryggeriklubben:BryggeriKlubben@db/inventory'


class Inventory(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.VARCHAR, nullable=True)
    alpha = db.Column(db.FLOAT, nullable=True)
    amount = db.Column(db.FLOAT, nullable=False)
    date = db.Column(db.DATE)
    type = db.Column(db.VARCHAR, nullable=False)


@app.route('/inventory', methods=['GET'])
def inventory():
    if request.method == 'GET':
        results = Inventory.query.limit(20).offset(0).all()

        json_result = []
        for result in results:
            data = {
                'id': result.id,
                'name': result.name,
                'description': result.description,
                'alpha': result.alpha,
                'amount': result.amount,
                'date': result.date,
                'type': result.type
            }
            json_result.append(data)

        return jsonify(items=json_result)

@app.route('/inventory/<int:id>', methods=['PUT', 'GET'])
def update_inventory(inventory_id):
    if request.method == 'PUT':
        results = Inventory.query.filter_by(id=inventory_id).first()

        json_result = {
                'id': results.id,
                'name': results.name,
                'description': results.description,
                'alpha': results.alpha,
                'amount': results.amount,
                'date': results.date,
                'type': results.type
            }
        return jsonify(items=json_result)
    #if request.method == 'GET':

@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory_item(id):
    if request.method == 'DELETE':
        db.session.delete(Inventory.query.get(id))
        db.session.commit()
    return jsonify({'result':true})

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
