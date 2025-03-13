import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1/(1+np.exp(-z))
class LogisticRegression:
    def __init__(self,learning_rate=0.01,n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights =  None
        self.bias = None

    def fit(self,X,y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):

            z= np.dot(X,self.weights)+self.bias
            y_pred =sigmoid(z)

            dw = (1/n_samples)*np.dot(X.T,(y_pred-y))
            db = (1/n_samples)*np.sum(y_pred-y)

            self.weights-=self.learning_rate*dw
            self.bias-=self.learning_rate*db

    def predict_proba(self,X):
        z = np.dot(X,self.weights)+self.bias
        return sigmoid(z)

    def predict(self,X,threshold=0.5):
        probability = self.predict_proba(X)
        return (probability>threshold).astype(int)
    
from sklearn.datasets import make_classification

X,y = make_classification(n_samples=100,n_features=2,n_informative=2,n_redundant=0, n_clusters_per_class=1, random_state=42)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Synthetic Dataset')
plt.show()

model = LogisticRegression(learning_rate=0.1, n_iterations=1000)
model.fit(X, y)

# Print the learned parameters
print("Coefficients (slopes):", model.weights)
print("Intercept (bias):", model.bias)

# Predict on the training data
predictions = model.predict(X)

# Calculate accuracy
accuracy = np.mean(predictions == y)
print("Accuracy:", accuracy)

x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01),
                       np.arange(x2_min, x2_max, 0.01))

# Predict over the grid
grid = np.c_[xx1.ravel(), xx2.ravel()]
Z = model.predict(grid)
Z = Z.reshape(xx1.shape)

# Plot
plt.contourf(xx1, xx2, Z, alpha=0.3, cmap='bwr')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Decision Boundary')
plt.show()