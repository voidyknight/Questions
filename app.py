from flask import Flask, render_template, request, redirect, url_for
import questions
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def questionStuff():

#names will be changed as css is created
    if request.method == "POST":
        question = request.form["question"]
        if question != None:
            answer = questions.main(question)
            sortedict =  sorted(answer, key=answer.get, reverse=True)
            return render_template("answer.html", keys = sortedict, values = answer.values())
    return render_template("main.html");

@app.route("/about")
def about():
    #return render_template("about.html")
    return redirect(url_for("/"))

if __name__ == "__main__":
    app.debug = True
    app.run()
