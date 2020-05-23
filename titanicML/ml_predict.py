def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.save','rb'))
    prediction = randomforest.predict(x)
    if prediction == 0:
        prediction = "did not survive"
    elif prediction == 1:
        prediction = "survived"
    else:
        prediction = 'error'
    return prediction