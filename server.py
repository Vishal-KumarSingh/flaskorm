from flask import Flask, render_template, request, redirect, url_for , jsonify
import sqlite3
from flask_sqlalchemy import SQLAlchemy  
import os
from flask_marshmallow import Marshmallow

curdir = os.getcwd() 
dbpath = "nobel_winners_cleaned_api_test.db"

abspath = "sqlite:///" + os.path.join(curdir , dbpath)
print(dbpath)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = abspath
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class Winner(db.Model):
    __tablename__ = 'winners'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    country = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    date_of_death = db.Column(db.String)
    gender = db.Column(db.String)
    link = db.Column(db.String)
    name = db.Column(db.String)
    place_of_birth = db.Column(db.String)
    place_of_death = db.Column(db.String)
    text = db.Column(db.Text)
    year = db.Column(db.Integer)
    award_age = db.Column(db.Integer)
    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"\
            % (self.name, self.category, self.year)
    
marsh = Marshmallow(app)
class WinnerSchema(marsh.Schema):
    class Meta():
        model= Winner
        fields = ('id' , 'category', 'country', 'date_of_birth', 'date_of_death',
                  'gender', 'link', 'name', 'place_of_birth', 'place_of_death', 'text', 'year', 'award_age')
multiwinner_schema = WinnerSchema(many=True)

@app.route("/", methods=["GET"])
def index():
    search_query = request.args.get('search', '')  
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_query:
        winners_pagination = Winner.query.filter(
            (Winner.name.ilike(f"%{search_query}%")) |
            (Winner.category.ilike(f"%{search_query}%"))
        ).paginate(page=page, per_page=per_page, error_out=False)
    else:
        winners_pagination = Winner.query.paginate(page=page, per_page=per_page, error_out=False)

    winners = winners_pagination.items
    result = multiwinner_schema.dump(winners)
    
    return render_template('index.html', winners=result, pagination=winners_pagination)

@app.route("/api/", methods=["GET"])
def api_get_winners():
    search_query = request.args.get('search', '')  
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_query:
        winners_pagination = Winner.query.filter(
            (Winner.name.ilike(f"%{search_query}%")) |
            (Winner.category.ilike(f"%{search_query}%"))
        ).paginate(page=page, per_page=per_page, error_out=False)
    else:
        winners_pagination = Winner.query.paginate(page=page, per_page=per_page, error_out=False)

    winners = winners_pagination.items
    result = multiwinner_schema.dump(winners)
    return result

@app.route("/add", methods=["GET", "POST"])
def add_winner():
    if request.method == "POST":
        new_winner = Winner(
            category=request.form["category"],
            country=request.form["country"],
            date_of_birth=request.form["date_of_birth"],
            date_of_death=request.form["date_of_death"],
            gender=request.form["gender"],
            link=request.form["link"],
            name=request.form["name"],
            place_of_birth=request.form["place_of_birth"],
            place_of_death=request.form["place_of_death"],
            text=request.form["text"],
            year=request.form["year"],
            award_age=request.form["award_age"]
        )
        db.session.add(new_winner)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_winner.html")


# API Route to Add a New Winner
@app.route("/api/add", methods=["POST"])
def api_add_winner():
    data = request.get_json()

    new_winner = Winner(
        category=data["category"],
        country=data["country"],
        date_of_birth=data["date_of_birth"],
        date_of_death=data["date_of_death"],
        gender=data["gender"],
        link=data["link"],
        name=data["name"],
        place_of_birth=data["place_of_birth"],
        place_of_death=data["place_of_death"],
        text=data["text"],
        year=data["year"],
        award_age=data["award_age"]
    )
    db.session.add(new_winner)
    db.session.commit()
    
    return jsonify({"message": "Winner added successfully!"}), 201

# API Route to Delete a Winner
@app.route("/api/delete/<int:winner_id>", methods=["DELETE"])
def api_delete_winner(winner_id):
    winner = Winner.query.get_or_404(winner_id)
    db.session.delete(winner)
    db.session.commit()

    return jsonify({"message": "Winner deleted successfully!"})

# API Route to Update a Winner
@app.route("/api/update/<int:winner_id>", methods=["PUT"])
def api_update_winner(winner_id):
    winner = Winner.query.get_or_404(winner_id)
    data = request.get_json()
    winner.category = data["category"]
    winner.country = data["country"]
    winner.date_of_birth = data["date_of_birth"]
    winner.date_of_death = data["date_of_death"]
    winner.gender = data["gender"]
    winner.link = data["link"]
    winner.name = data["name"]
    winner.place_of_birth = data["place_of_birth"]
    winner.place_of_death = data["place_of_death"]
    winner.text = data["text"]
    winner.year = data["year"]
    winner.award_age = data["award_age"]
    
    db.session.commit()
    return jsonify({"message": "Winner updated successfully!"})


@app.route("/delete/<int:winner_id>", methods=["POST"])
def delete_winner(winner_id):
    winner = Winner.query.get_or_404(winner_id)
    db.session.delete(winner)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/update/<int:winner_id>", methods=["GET", "POST"])
def update_winner(winner_id):
    winner = Winner.query.get_or_404(winner_id)  

    if request.method == "POST":

        winner.category = request.form["category"]
        winner.country = request.form["country"]
        winner.date_of_birth = request.form["date_of_birth"]
        winner.date_of_death = request.form["date_of_death"]
        winner.gender = request.form["gender"]
        winner.link = request.form["link"]
        winner.name = request.form["name"]
        winner.place_of_birth = request.form["place_of_birth"]
        winner.place_of_death = request.form["place_of_death"]
        winner.text = request.form["text"]
        winner.year = request.form["year"]
        winner.award_age = request.form["award_age"]
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("update_winner.html", winner=winner)

if __name__ == "__main__":
    app.run(debug=True , port=6000)