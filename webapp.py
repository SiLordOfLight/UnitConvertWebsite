from flask import Flask, url_for, render_template

app = Flask(__name__)

# global pages = ["Home", "Page 1", "Page 2"]

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template('home.html')

@app.route("/len-n-dist")
def render_cop():
    units = ["Miles","Kilometers","Feet","Meters"]
    return render_template('length-and-distance.html', units=units)

# @app.route("/currency")
# def render_psum():
#     return render_template('currency.html')
#
# @app.route("/time")
# def render_wikiPage():
#     return render_template('time.html')
#
# @app.route("/weight")
# def render_wikiPage():
#     return render_template('weight.html')

@app.route("/out")
def render_wikiPage():
    vals = request.args
    return render_template('out.html', inVal1 = vals["val1"], inVal2 = vals["val2"], inUnit1 = vals["unit1"], inUnit2 = vals["unit2"])

if __name__=="__main__":
    app.run(debug=False, port=54321)
