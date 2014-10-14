from flask import Flask, render_template, request
import questions
app = Flask(__name__)



def first10Keys(dict):
    sortedict =  sorted(dict, key=dict.get, reverse=True)
    keys = []
    for x in range(10):
        keys.append(sortedict[x])
    return keys

def first10Vals(dict):
    rawVals = dict.values()
    rawVals.sort()
    rawVals.reverse()
    vals = []
    for x in range(10):
        vals.append(rawVals[x])
    return vals


@app.route("/", methods = ["GET", "POST"])
def questionStuff():
#names will be changed as css is created
    if request.method == "POST":
        question = request.form["question"]
        if question != None:
            answer = questions.main(question)
            return render_template("answer.html", keys = first10Keys(answer), values = first10Vals(answer))
    return render_template("main.html");

if __name__ == "__main__":
    app.debug = True
    app.run()
