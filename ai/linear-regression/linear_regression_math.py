class LinearRegression:
    def __init__(self):
        self.m = 0  # Slope
        self.b = 0  # Intercept

    def fit(self, X, y):
        n = len(X)
        sum_x = sum(X)
        sum_y = sum(y)
        sum_xy = sum(x * y for x, y in zip(X, y))
        sum_x2 = sum(x * x for x in X)
        
        self.m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        self.b = (sum_y - self.m * sum_x) / n

    def predict(self, X):
        return [self.m * x + self.b for x in X]

# Example Usage
X_train = [1, 2, 3, 4, 5]
y_train = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X_train, y_train)

X_test = [6, 7, 8]
y_pred = model.predict(X_test)
print(y_pred)  # Expected output: [12, 14, 16]
