import pickle

import numpy as np
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

menu = [{"name": "Лаба 1", "url": "p_lab1"},
        {"name": "Лаба 2", "url": "p_lab2"},
        {"name": "Лаба 3", "url": "p_lab3"},
        {"name": "Лаба 4", "url": "p_lab4"}]

loaded_model_lin_reg = pickle.load(open('model/LinR.kuz', 'rb'))
loaded_model_log_reg = pickle.load(open('model/LogR.kuz', 'rb'))
loaded_model_knn = pickle.load(open('model/KNN.kuz', 'rb'))
loaded_model_decision_tree = pickle.load(open('model/DT.kuz', 'rb'))

pengu_species = {
    0: "Adelie",
    1: "Gentoo",
}

@app.route('/api1', methods=['get'])
def get_mark():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['number_courses']),
                       float(request_data['time_study']),]])
    pred = loaded_model_lin_reg.predict(X_new)

    return jsonify(Marks=pred[0][0])

@app.route('/api2', methods=['get'])
def get_penguin1():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['island']),
                       float(request_data['bill_length_mm']),
                       float(request_data['bill_depth_mm']),
                       float(request_data['flipper_length_mm']),
                       float(request_data['body_mass_g']),
                       float(request_data['year']),]])
    pred = pengu_species[loaded_model_log_reg.predict(X_new)[0]]

    return jsonify(species=pred)

@app.route('/api3', methods=['get'])
def get_penguin2():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['island']),
                       float(request_data['bill_length_mm']),
                       float(request_data['bill_depth_mm']),
                       float(request_data['flipper_length_mm']),
                       float(request_data['body_mass_g']),
                       float(request_data['year']),]])
    pred = pengu_species[loaded_model_knn.predict(X_new)[0]]

    return jsonify(species=pred)

@app.route('/api4', methods=['get'])
def get_penguin():
    request_data = request.get_json()
    X_new = np.array([[float(request_data['island']),
                       float(request_data['bill_length_mm']),
                       float(request_data['bill_depth_mm']),
                       float(request_data['flipper_length_mm']),
                       float(request_data['body_mass_g']),
                       float(request_data['year']),]])
    pred = pengu_species[loaded_model_decision_tree.predict(X_new)[0]]

    return jsonify(species=pred)

@app.route("/")
def index():
    return render_template('index.html', title="Лабораторные работы, выполненные Кузенковым Б. А.", menu=menu)


@app.route("/p_lab1", methods=['POST', 'GET'])
def f_lab1():
    if request.method == 'GET':
        return render_template('lab1.html', title="Линейная регрессия", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),]])
        pred = loaded_model_lin_reg.predict(X_new)
        return render_template('lab1.html', title="Линейная регрессия", menu=menu,
                               class_model=round(pred[0][0], 2))

@app.route("/p_lab2", methods=['POST', 'GET'])
def f_lab2():
    if request.method == 'GET':
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),
                           float(request.form['list4']),
                           float(request.form['list5']),
                           float(request.form['list6']),]])
        pred = pengu_species[loaded_model_log_reg.predict(X_new)[0]]
        return render_template('lab2.html', title="Логистическая регрессия", menu=menu,
                               class_model=pred)


@app.route("/p_lab3", methods=['POST', 'GET'])
def f_lab3():
    if request.method == 'GET':
        return render_template('lab3.html', title="Метод K-ближайших соседей kNN", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),
                           float(request.form['list4']),
                           float(request.form['list5']),
                           float(request.form['list6']), ]])
        pred = pengu_species[loaded_model_knn.predict(X_new)[0]]
        return render_template('lab3.html', title="Метод K-ближайших соседей kNN", menu=menu,
                               class_model=pred)

@app.route("/p_lab4", methods=['POST', 'GET'])
def f_lab4():
    if request.method == 'GET':
        return render_template('lab4.html', title="Дерево решений", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),
                           float(request.form['list4']),
                           float(request.form['list5']),
                           float(request.form['list6']), ]])
        pred = pengu_species[loaded_model_decision_tree.predict(X_new)[0]]
        return render_template('lab4.html', title="Дерево решений", menu=menu,
                               class_model=pred)


if __name__ == "__main__":
    app.run(debug=True)
