from flask import Flask, render_template,request
import pandas as pd
import pickle

model = pickle.load(open("UsedCar.pkl", 'rb'))
app = Flask(__name__)
car = pd.read_csv('Cleaned Car.csv')

@app.route("/")
def index():
    Brands = sorted(car['brand'].unique())
    Car_models = sorted(car['model'].unique())
    Km_driven = sorted(car['km_driven'].unique())
    fuel = sorted(car['fuel'].unique())
    Mileage = sorted(car['mileage'].unique())
    Engine = sorted(car['engine'].unique())
    Seats = sorted(car['seats'].unique())
    years = sorted(car['No_of_years'].unique())

    return render_template("index.html", Brands=Brands, Car_models=Car_models, Km_driven=Km_driven, fuel=fuel,
                           Mileage=Mileage, Engine=Engine, Seats=Seats, years=years)

@app.route(rule='/predict', methods=['POST'])
def predict():
    Brand = request.form.get('Brand')
    model = request.form.get("model")
    km_driven = int(request.form.get('km_driven'))
    Fuel= request.form.get('Fuel')
    Mileages = request.form.get('Mileages')
    engine = request.form.get("engine")
    Capacity = request.form.get("Capacity")
    year = int(request.form.get('year'))
    print(Brand,model,km_driven,Fuel,Mileages,engine,Capacity,year)

    prediction = model.predict(pd.DataFrame([[Brand,model,km_driven,Fuel,Mileages,engine,Capacity,year]], columns=['Brand',
    'model','km_driven','Fuel','Mileages','engine','Capacity','year']))

    return str(prediction[0])



if __name__ == "__main__":
    app.run(debug=True)
