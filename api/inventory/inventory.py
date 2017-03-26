from flask import Flask, request, jsonify, flash
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

    def __init__(self, _name, _description, _alpha, _amount, _date, _type):
        self.name = _name
        self.description = _description
        self.alpha = _alpha
        self.amount = _amount
        self.date = _date
        self.type = _type


@app.route('/inventory/', methods=['GET', 'POST'])
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

    if request.method == 'POST':
        results = Inventory.query.limit(1).offset(0).all()
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

        ## if not json_result[1] == request.form['name'] and not json_result[3] == request.form['alpha']:
        ##   return 'Did not work'
        ## else:
            ingredient = Inventory(request.form['name'], request.form['description'], request.form['alpha'], request.form['amount'], request.form['date'], request.form['type'])
            db.session.add(ingredient)
            db.session.commit()
        return 'Added.', 204


@app.route('/inventory/<int:inventory_id>/', methods=['PUT', 'GET', 'DELETE'])
def update_inventory(inventory_id):
    if request.method == 'GET':
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
        ingredient = Inventory(request.form['name'], request.form['description'], request.form['alpha'],
                               request.form['amount'], request.form['date'], request.form['type'])

        results.name = request.json.get('name', results.name)
        results.description = request.json.get('description', results.description)
        results.alpha = request.json.get('alpha', results.alpha)
        results.amount = request.json.get('amount', results.amount)
        results.date = request.json.get('date', results.date)
        results.type = request.json.get('type', results.type)
        db.session.commit()
        return jsonify({'results': results})

    if request.method == 'DELETE':
        result = Inventory.query.filter_by(id=inventory_id).first()
        db.session.delete(result)
        db.session.commit()
        return '', 204


# @app.route('/inventory/<int:inventory_id>/', methods=['DELETE'])
# def delete_item(inventory_id):


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
