
from flask import Flask,render_template

webpage=Flask(__name__)
@webpage.route("/")
def my_welcome_page():
    return render_template("home.html")
@webpage.route("/sarees")
def my_welcome_page2():
    return render_template("sarees.html")
@webpage.route("/halfsarees")
def my_welcome_page3():
    return render_template("halfsarees.html")
@webpage.route("/chudidhars")
def my_welcome_page4():
    return render_template("chudidhars.html")
@webpage.route("/kids")
def my_welcome_page5():
    return render_template("kids.html")
@webpage.route("/frocks")
def my_welcome_page6():
    return render_template("frocks.html")

if __name__=="__main__":
  webpage.run(host="127.0.0.2",port=5001,debug=True)

