from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personregister.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100), nullable=False)
    alder = db.Column(db.Integer, nullable=False)
    telefonnummer = db.Column(db.String(20), nullable=False)
    land = db.Column(db.String(100), nullable=False)

def init_db():
    """Initialiserar databasen och seedar den med startdata."""
    with app.app_context():
        db.create_all()
        if not Person.query.first():
            personer = [
                Person(namn='Anna Svensson', alder=30, telefonnummer='010-123 45 67', land='Sverige'),
                Person(namn='Karl Johansson', alder=45, telefonnummer='010-234 56 78', land='Sverige'),
            ]
            db.session.bulk_save_objects(personer)
            db.session.commit()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/allpersons')
def allpersons():
    personer = Person.query.all()
    return render_template('allpersons.html', personer=personer)

@app.route('/person/<int:id>')
def person(id):
    person = Person.query.get_or_404(id)
    return render_template('person.html', person=person)

# Anropa init_db() här för att säkerställa att databasen är initialiserad
init_db()

if __name__ == '__main__':
    app.run(debug=True)
