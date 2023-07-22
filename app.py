from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    choice = int(request.form['choice'])
    conversion_result = ""

    if choice == 1:
        # Weight Conversion: Pounds to Kilogram
        pounds = float(request.form['value'])
        kilograms = pounds * 0.45359237
        conversion_result = f"{pounds} Pounds is approximately {kilograms:.2f} Kilograms."

    elif choice == 2:
        # Distance Conversion: Miles to Kilometers
        miles = float(request.form['value'])
        kilometers = miles * 1.60934
        conversion_result = f"{miles} Miles is approximately {kilometers:.2f} Kilometers."

    elif choice == 3:
        # Temperature Conversion: Fahrenheit to Celsius
        fahrenheit = float(request.form['value'])
        celsius = (fahrenheit - 32) * 5/9
        conversion_result = f"{fahrenheit} Fahrenheit is approximately {celsius:.2f} Celsius."

    return render_template('index.html', conversion_result=conversion_result)

if __name__ == '__main__':
    app.run(debug=True)
