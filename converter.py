# All lengths based on cm
baseRates = {"Miles":160934, "Kilometers": 100000, "Feet":30.48, "Meters":100}

# All currencies based on USD
baseRates['US Dollars'] = 1
baseRates['British Pounds'] = 1.31
baseRates['Euros'] = 1.15
baseRates['Mexican Pesos'] = 0.053

# All times based on s
baseRates['Seconds'] = 1
baseRates['Minutes'] = 60
baseRates['Hours'] = 3600
baseRates['Days'] = 86400
baseRates['Weeks'] = 604800
baseRates['Years'] = 31449600

# All weights based on g
baseRates['Pounds'] = 453.592
baseRates['Kilograms'] = 1000
baseRates['Ounces'] = 28.3495
baseRates['Grams'] = 1

# All weights based on Earth weight
baseRates['lbs on Earth'] = 1
baseRates['lbs on Mars'] = 0.376
baseRates['lbs on the Moon'] = 0.016
baseRates['lbs on Ceres'] = 0.029
baseRates['lbs on Mercury'] = 0.38
baseRates['lbs on Titan'] = 0.14
baseRates['lbs on Pluto'] = 0.063

# All energies based on J
baseRates['Joules'] = 1
baseRates['Kilojoules'] = 1000
baseRates['Calories'] = 4.184
baseRates['Kilocalories'] = 4184
baseRates['Kilowatt Hours'] = 3600000

def convert(inVal, inUni, outUni):
    inUnitMult = baseRates[inUni]
    outUnitDiv = baseRates[outUni]

    return (inVal * inUnitMult)/outUnitDiv

# x mi * y cm/mi = z cm
# z cm / w cm/km = v km
