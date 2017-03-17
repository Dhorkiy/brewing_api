from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bryggeriklubben:BryggeriKlubben@mysql/inventory'

class Inventory(db.model):
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

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
