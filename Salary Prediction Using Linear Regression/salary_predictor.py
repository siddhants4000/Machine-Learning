import joblib
model= joblib.load('salary.pk1')
exp=int(input("Enter Experience for Salary to Predict: "))
predict= model.predict([[exp]])
print(predict)