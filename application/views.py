from flask import Response, json, render_template, request
from .model import User, Course, Enrollment
from . import app, db

course_data = [
    {"courseID": "1111", "title": "PHP 101",
     "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1",
     "description": "Intro to Java Programming", "credits": 4, "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201",
     "description": "Advanced PHP Programming", "credits": 3, "term": "Fall"},
    {"courseID": "4444", "title": "Angular 1",
     "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4, "term": "Fall"}]


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):

    return render_template("courses.html", course_data=course_data, term=term)


@app.route("/enrollment")
def enrollment():
    course_id = request.args.get('courseID')
    title = request.args.get('title')
    term = request.args.get('term')
    data = {'term': term, 'course_id': course_id, 'title': title}
    return render_template("enrollment.html", data=data)


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = course_data
    else:
        jdata = course_data[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Christian", last_name="Hur",
    #      email="christian@uta.com", password="abc1234").save()
    # User(user_id=2, first_name="Mary", last_name="Jane",
    #      email="mary.jane@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
