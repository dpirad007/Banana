import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Regression:

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def linear_regression(self, X, y):
        self.X, self.y = X, y
        m = 5
        c = 0
        n = self.X.shape[0]
        for _ in range(self.epochs):
            b_gradient = -2 * np.sum(self.y - (m*self.X + c)) / n
            m_gradient = -2 * np.sum(self.X*(self.y - (m*self.X + c))) / n
            c = c - (self.learning_rate * b_gradient)
            m = m - (self.learning_rate * m_gradient)
        self.m, self.c = m, c

    def predict(self, X):
        return self.m*X+self.c


# df = pd.read_csv("weight-height.csv")
# df = df.drop(['Gender'], axis=1)

# X = df["Height"]
# y = df["Weight"]


np.random.seed(42)
X = np.array(sorted(list(range(5))*20)) + np.random.normal(size=100, scale=0.5)
y = np.array(sorted(list(range(5))*20)) + \
    np.random.normal(size=100, scale=0.25)


reg = Regression(learning_rate=0.1, epochs=1000)
reg.linear_regression(X, y)
plt.scatter(X, y)
print(reg.predict(3))
plt.plot(X, reg.predict(X))
plt.show()
