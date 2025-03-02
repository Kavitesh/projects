import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Given dataset
data = np.array([
    [37, 18, 26, 67, 57, 39, 31],
    [95, 54, 24, 79, 80, 47, 49],
    [73, 87, 90, 25, 76, 85, 56],
    [59, 73, 24, 62, 15, 34, 59],
    [15, 80, 27, 57, 14, 86, 66],
    [15, 65, 75, 83, 26, 8, 55],
    [5, 69, 44, 90, 36, 77, 70],
    [86, 84, 77, 1, 40, 84, 61],
    [60, 24, 6, 67, 67, 18, 19],
    [70, 48, 48, 5, 5, 43, 47],
    [2, 22, 3, 54, 3, 16, 26],
    [96, 98, 6, 28, 39, 70, 53],
    [83, 94, 90, 30, 69, 53, 53]
])

# Split features (X) and target (y)
X = data[:, :-1]
y = data[:, -1]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

print(model.coef_)
# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
# Extract model coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

# Display the regression equation
feature_names = [
    "Zone_Threat_Level", "Human_Density", "Young_Male_Density",
    "Suspicious_People_Density", "Minor_Density", "Heavy_Vehicle_Percentage"
]

equation = "Threat_Level = {:.4f}".format(intercept)
for coef, name in zip(coefficients, feature_names):
    equation += " + ({:.4f} * {})".format(coef, name)

print("Final Prediction Equation:")
print(equation) 

# Threat Level = w0+w1(Zone Threat Level)+w2(Human Density)+w3(Young Male Density)+w4(Suspicious People Density)+w5(Minor Density)+w6(Heavy Vehicle Percentage)
#w0=-10
#w1 = .3
#w2= .1
#w3= .3
#w4= .5
#w5= -.5
#w6= .4
