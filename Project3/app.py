from flask import Flask,request,render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('C:/Users/Asus/PycharmProjects/flaskProject3/templates/model7.pkl')


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def predict():  # put application's code here
    if request.method == 'POST':
        type1 = float(request.form.get('type1'))
        type2 = float(request.form.get('type2'))
        hp = float(request.form['health'])
        attack = float(request.form.get('attack'))
        defense = float(request.form.get('defense'))
        sp_attack = float(request.form.get('spattack'))
        sp_defense = float(request.form.get('spdefense'))
        speed = float(request.form.get('speed'))

        if type1 == 'Blastoise':
            type1 = 0
        elif type1 == 'Bug':
            type1 = 1
        elif type1 == 'Dark':
            type1 = 2
        elif type1 == 'Dragon':
            type1 = 3
        elif type1 == 'Electric':
            type1 = 4
        elif type1 == 'Fairy':
            type1 = 5
        elif type1 == 'Fighting':
            type1 = 6
        elif type1 == 'Fire':
            type1 = 7
        elif type1 == 'Flying':
            type1 = 8
        elif type1 == 'Ghost':
            type1 = 9
        elif type1 == 'Grass':
            type1 = 10
        elif type1 == 'Ground':
            type1 = 11
        elif type1 == 'Ice':
            type1 = 12
        elif type1 == 'Normal':
            type1 = 13
        elif type1 == 'Poison':
            type1 = 14
        elif type1 == 'Psychic':
            type1 = 15
        elif type1 == 'Rock':
            type1 = 16
        elif type1 == 'Steel':
            type1 = 17
        elif type1 == 'Water':
            type1 = 18


        if type2 == 'Blastoise':
            type2 = -1
        elif type2 == 'Bug':
            type2 = 0
        elif type2 == 'Dark':
            type2 = 1
        elif type2 == 'Dragon':
            type2 = 2
        elif type2 == 'Electric':
            type2 = 3
        elif type2 == 'Fairy':
            type2 = 4
        elif type2 == 'Fighting':
            type2 = 5
        elif type2 == 'Fire':
            type2 = 6
        elif type2 == 'Flying':
            type2 = 7
        elif type2 == 'Ghost':
            type2 = 8
        elif type2 == 'Grass':
            type2 = 9
        elif type2 == 'Ground':
            type2 = 10
        elif type2 == 'Ice':
            type2 = 11
        elif type2 == 'Normal':
            type2 = 12
        elif type2 == 'Poison':
            type2 = 13
        elif type2 == 'Psychic':
            type2 = 14
        elif type2 == 'Rock':
            type2 = 15
        elif type2 == 'Steel':
            type2 = 16
        elif type2 == 'Water':
            type2 = 17


        total = hp+attack + defense +sp_attack+ sp_defense+speed

        prediction = model.predict(np.array([[type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,total]]))


        if prediction == 0:
            prediction = "COMMON"
        else:
            prediction="LEGENDARY"

        return render_template("prediction.html", prediction_text="This Pokemon is {}".format(prediction))

    else:
        return render_template("prediction.html")



if __name__ == '__main__':
    app.debug = True
    app.run()