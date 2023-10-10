from flask import Flask
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        return f'Name: {animal.name}<br>Species: {animal.species}<br>Zookeeper: {animal.zookeeper.name}<br>Enclosure: {animal.enclosure.environment}'
    else:
        return 'Animal not found'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        animals = [animal.name for animal in zookeeper.animals.all()]
        return f'Name: {zookeeper.name}<br>Birthday: {zookeeper.birthday}<br>Animals: {", ".join(animals)}'
    else:
        return 'Zookeeper not found'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        animals = [animal.name for animal in enclosure.animals.all()]
        return f'Environment: {enclosure.environment}<br>Open to Visitors: {enclosure.open_to_visitors}<br>Animals: {", ".join(animals)}'
    else:
        return 'Enclosure not found'

if __name__ == '__main':
    app.run(port=5555, debug=True)
