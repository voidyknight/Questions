from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():

#names will be changed as css is created
    question = request.args.get("question", None)
    sub = request.args.get("submit", None)

    if sub == "submit" and question != None:
        question = question.replace(" ", "~")
        return redirect(url_for("answer/"+question))
    return render_template("main.html");

@app.route("/answer/<question>")
def answer(question = None):
    #answer = answer(question)
    #return render_template("answer.html", ans = answer)
    pass

@app.route("/about")
def about():
    #return render_template("about.html")
    pass

if __name__ == "__main__":
    app.debug = True
    app.run()
