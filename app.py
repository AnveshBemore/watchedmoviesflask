from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)

mydb=mysql.connector.connect(
    host="localhost",
    user="AnveshBemore",
    password="Anvesh@123",
    database="movies"
)

@app.route("/")
def index():
    return render_template("home.html")
@app.route("/add")
def add():

   return render_template("add.html")

@app.route("/save",methods=["GET","POST"])
def save():
    if request.method=="POST":
        mycursor=mydb.cursor()
        userdetails=request.form
        movie=userdetails['name']
        genre=userdetails['genre']
        ww=userdetails['ww']
        sd=userdetails['sd']
        fl=userdetails['fl']
        q="insert into watchedmovies(Movie,Genre,Worth_Watching,Special_Details,free_link) values(%s,%s,%s,%s,%s)"
        v=(movie,genre,ww,sd,fl)
        mycursor.execute(q,v)
        mydb.commit()
        z=movie+" "+genre+" "+ww+" "+sd+" "+fl+" "+"added successfully"
        return render_template("success.html",msg=z)


@app.route("/view")
def view():
    mycursor=mydb.cursor()
    s="select * from watchedmovies"
    mycursor.execute(s)
    data=mycursor.fetchall()
    return render_template("view.html",data=data)


@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/searchvalue",methods=["GET","POST"])
def searchvalue():
    if request.method =="POST":
        mycursor=mydb.cursor()
        s="select * from watchedmovies where Movie=%s"
        v=[request.form["search"]]
        mycursor.execute(s,v)
        data=mycursor.fetchall()
        return render_template("view.html",data=data)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deletemovie",methods=["POST","GET"])
def deletemovie():
    if request.method=="POST":
        v =[request.form["delmovie"]]
        mycursor = mydb.cursor()
        q = "delete from watchedmovies where movie=%s"
        mycursor.execute(q,v)
        mydb.commit()
        z=v[0]+" deleted successfully"
        return render_template("success.html",msg=z)


if __name__== "__main__":
    app.run(debug=True)