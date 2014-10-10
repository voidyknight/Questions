import flask

@app.route("/")
def index():
    render_template("index.html");
