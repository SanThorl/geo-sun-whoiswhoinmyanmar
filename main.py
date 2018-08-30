from flask import Flask, render_template, request, redirect, url_for
import os 
from flask_sqlalchemy import SQLAlchemy 

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Personal.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "Who is Who in Myanmar"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

search = ""
@app.route('/', methods=['POST', 'GET'])
def search():
    people = Person.query.all()

    search = request.form['search']
    names = Person.query.order_by(Person.name).all()
    results = Person.query.filter(Person.name.contains(search)).all()
    return render_template("search.html", results=results)

@app.route('/aboutparli.html', methods=['POST', 'GET'])
def politician():
    politician = Person.query.filter(Person.profession=="politician").all()
    return render_template("aboutparli.html", politician=politician)

@app.route('/aboutwriter.html', methods=['POST', 'GET'])
def writer():
    writer = Person.query.filter(Person.profession=="writer").all()
    return render_template("aboutwriter.html", writer=writer)

@app.route('/aboutdirector.html', methods=['POST', 'GET'])
def director():
    director = Person.query.filter(Person.profession=="director").all()
    return render_template("aboutdirector.html", director=director)
    
@app.route('/aboutactor.html', methods=['POST', 'GET'])
def actor():
    actor = Person.query.filter(Person.profession=="actor").all()
    return render_template("aboutactor.html", actor=actor)

@app.route('/aboutsinger.html', methods=['POST', 'GET'])
def singer():
    singer = Person.query.filter(Person.profession=="singer").all()
    return render_template("aboutsinger.html", singer=singer)

@app.route("/about.html", methods=['POST', 'GET'])
def about():
    return render_template("about.html")

@app.route("/help.html", methods=['POST', 'GET'])
def help():
    return render_template("help.html")

@app.route("/method.html", methods=['POST', 'GET'])
def method():
    return render_template("method.html")

@app.route("/use.html", methods=['POST', 'GET'])
def use():
    return render_template("use.html")

@app.route("/contact.html", methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")

@app.route("/qa.html", methods=['POST', 'GET'])
def qa():
    return render_template("qa.html")

@app.route("/partner.html", methods=['POST', 'GET'])
def partner():
    return render_template("partner.html")

class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    profession = db.Column(db.String(30),nullable=False)
    image = db.Column(db.Text,nullable=False)
    contact = db.Column(db.Text,nullable=False)

    def __init__(self,*args,**kwargs):
        super(Person,self).__init__(*args,**kwargs)
    
    def __repr__(self):
        return "<Person: {}>".format(self.name)
if __name__=="__main__":
    app.run(debug=True)
