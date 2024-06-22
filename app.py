from flask import Flask, render_template, request
import os
import pickle

working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

app = Flask(__name__)
@app.route('/')
def main():

    return render_template('index.html')
@app.route('/parkinsons', methods=['POST'])
def ans1():
    parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
    fo= request.form['fo']
    fhi= request.form['fhi']
    flo = request.form['flo']
    Jitter_percent = request.form['jitter_percent']
    Jitter_Abs = request.form['jitter_abs']
    RAP = request.form['rap']
    PPQ = request.form['ppq']
    DDP = request.form['ddp']
    Shimmer = request.form['shimmer']
    Shimmer_dB = request.form['shimmer_db']
    APQ3 = request.form['apq3']
    APQ5 = request.form['apq5']
    APQ = request.form['apq']
    DDA = request.form['dda']
    NHR = request.form['nhr']
    HNR = request.form['hnr']
    RPDE = request.form['rpde']
    DFA = request.form['dfa']
    spread1 = request.form['spread1']
    spread2 = request.form['spread2']
    D2 = request.form['d2']
    PPE = request.form['ppe']

    user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

    user_input = [float(x) for x in user_input]

    parkinsons_prediction = parkinsons_model.predict([user_input])

    if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
    else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"


    print(parkinsons_diagnosis)
    return render_template('index.html', parkinsons_diagnosis=parkinsons_diagnosis)
@app.route('/heart', methods=['POST'])
def ans():
    age = request.form['age']
    sex= request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    user_input = [float(x) for x in user_input]

    heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
    else:
            heart_diagnosis = 'The person does not have any heart disease'

    print(heart_diagnosis)
    return render_template('index.html', heart_diagnosis=heart_diagnosis)
@app.route('/diabetes', methods=['POST'])
def ans2():
        pregnancies = request.form['pregnancies']
        glucose = request.form['glucose']
        blood_pressure = request.form['bloodPressure']
        skin_thickness = request.form['skinThickness']
        insulin = request.form['insulin']
        bmi = request.form['bmi']
        diabetes_pedigree_function = request.form['diabetesPedigreeFunction']
        age = request.form['age']
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        
        user_input = [float(x) for x in user_input]
        
        diabetes_prediction = diabetes_model.predict([user_input])
        
        if diabetes_prediction[0] == 1:
                diabetes_diagnosis = 'The person is diabetic'
        else:
                diabetes_diagnosis = 'The person is not diabetic'
        
        print(diabetes_diagnosis)
        return render_template('index.html', diabetes_diagnosis=diabetes_diagnosis)
if __name__ == '__main__':
    app.run(debug=True)    