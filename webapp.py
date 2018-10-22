from flask import Flask, url_for, render_template, request
import converter as conv

app = Flask(__name__)

# global pages = ["Home", "Page 1", "Page 2"]

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template('home.html')

@app.route("/len-n-dist")
def render_lnd():
    units = ["Miles","Kilometers","Feet","Meters"]

    try:
        # print("do 1")
        inputValue = float(request.args['val1'])
        inputUnit = request.args['unit1']
        outputUnit = request.args['unit2']
        result = conv.convert(inputValue, inputUnit, outputUnit)
        showResult = "%s %s -> %s %s" % (str(inputValue).rstrip('0').rstrip('.'), inputUnit, str(result).rstrip('0').rstrip('.'), outputUnit)
        # print(showResult)
        return render_template('length-and-distance.html', units=units, result=showResult)
    except Exception as e:
        # print(e)
        return render_template('length-and-distance.html', units=units, result="")

@app.route("/currency")
def render_currency():
    units = ["US Dollars","British Pounds","Euros","Mexican Pesos"]

    try:
        # print("do 1")
        inputValue = float(request.args['val1'])
        print(inputValue)
        inputUnit = request.args['unit1']
        outputUnit = request.args['unit2']
        result = conv.convert(inputValue, inputUnit, outputUnit)
        showResult = "%s %s -> %s %s" % (str(inputValue).rstrip('0').rstrip('.'), inputUnit, "{0:.2f}".format(result), outputUnit)
        # print(showResult)
        return render_template('currency.html', units=units, result=showResult)
    except Exception as e:
        # print(e)
        return render_template('currency.html', units=units, result="")

@app.route("/time")
def render_time():
    units = ["Seconds","Minutes","Hours","Days", "Weeks", "Years"]

    try:
        # print("do 1")
        inputValue = float(request.args['val1'])
        inputUnit = request.args['unit1']
        outputUnit = request.args['unit2']
        result = conv.convert(inputValue, inputUnit, outputUnit)
        showResult = "%s %s -> %s %s" % (str(inputValue).rstrip('0').rstrip('.'), inputUnit, str(result).rstrip('0').rstrip('.'), outputUnit)
        # print(showResult)
        return render_template('time.html', units=units, result=showResult)
    except Exception as e:
        # print(e)
        return render_template('time.html', units=units, result="")

@app.route("/weight")
def render_weight():
    units = ["Pounds","Kilograms","Ounces","Grams"]

    try:
        # print("do 1")
        inputValue = float(request.args['val1'])
        inputUnit = request.args['unit1']
        outputUnit = request.args['unit2']
        result = conv.convert(inputValue, inputUnit, outputUnit)
        showResult = "%s %s -> %s %s" % (str(inputValue).rstrip('0').rstrip('.'), inputUnit, str(result).rstrip('0').rstrip('.'), outputUnit)
        # print(showResult)
        return render_template('weight.html', units=units, result=showResult)
    except Exception as e:
        # print(e)
        return render_template('weight.html', units=units, result="")

@app.route("/planets")
def render_weight():
    units = ["lbs on Earth", "lbs on Mars", "lbs on the Moon", "lbs on Ceres", "lbs on Mercury", "lbs on Titan", "lbs on Pluto"]

    try:
        # print("do 1")
        inputValue = float(request.args['val1'])
        inputUnit = request.args['unit1']
        outputUnit = request.args['unit2']
        result = conv.convert(inputValue, inputUnit, outputUnit)
        showResult = "%s %s -> %s %s" % (str(inputValue).rstrip('0').rstrip('.'), inputUnit, str(result).rstrip('0').rstrip('.'), outputUnit)
        # print(showResult)
        return render_template('planets.html', units=units, result=showResult)
    except Exception as e:
        # print(e)
        return render_template('planets.html', units=units, result="")

@app.route("/energy")
def render_weight():
    units = ["Joules", "Kilojoules", "Calories", "Kilocalories", "Kilowatt Hour"]

    try:
        # print("do 1")
        inputValue = float(request.args['val1'])
        inputUnit = request.args['unit1']
        outputUnit = request.args['unit2']
        result = conv.convert(inputValue, inputUnit, outputUnit)
        showResult = "%s %s -> %s %s" % (str(inputValue).rstrip('0').rstrip('.'), inputUnit, str(result).rstrip('0').rstrip('.'), outputUnit)
        # print(showResult)
        return render_template('energy.html', units=units, result=showResult)
    except Exception as e:
        # print(e)
        return render_template('energy.html', units=units, result="")

if __name__=="__main__":
    app.run(debug=False, port=54321)
