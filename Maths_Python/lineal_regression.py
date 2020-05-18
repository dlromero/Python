from sklearn.linear_model import LogisticRegression
import numpy as np

x = np.array([0.5, 0.75, 1, 1.25, 1.5, 1.75, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 4.25, 4.5,
              4.75, 5, 5.5]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0,
              1, 0, 1, 1, 1, 1, 1, 1])


regression_logistic = LogisticRegression()

regression_logistic.fit(x, y)
x_new = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
prediction = regression_logistic.predict(x_new)
print(prediction)

prediction_probability = regression_logistic.predict_proba(x_new)
print(prediction_probability)
print(prediction_probability[:1])