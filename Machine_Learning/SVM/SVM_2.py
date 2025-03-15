import numpy as np
import matplotlib.pyplot as plt

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iterations=1000, problem_type='classification'):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iterations
        self.problem_type = problem_type
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        if self.problem_type == 'classification':
            y_ = np.where(y <= 0, -1, 1)
        else:
            y_ = y
        
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                if self.problem_type == 'classification':
                    condition = y_[idx] * (np.dot(x_i, self.weights) + self.bias) >= 1
                    if condition:
                        dw = 2 * self.lambda_param * self.weights
                        db = 0
                    else:
                        dw = 2 * self.lambda_param * self.weights - np.dot(x_i, y_[idx])
                        db = -y_[idx]
                else:
                    epsilon = 0.1
                    prediction = np.dot(x_i, self.weights) + self.bias
                    error = prediction - y_[idx]
                    if abs(error) <= epsilon:
                        dw = 2 * self.lambda_param * self.weights
                        db = 0
                    else:
                        dw = 2 * self.lambda_param * self.weights + x_i * np.sign(error)
                        db = np.sign(error)
                
                self.weights -= self.lr * dw
                self.bias -= self.lr * db
    
    def predict(self, X):
        output = np.dot(X, self.weights) + self.bias
        if self.problem_type == 'classification':
            return np.sign(output)
        return output
    
    def score(self, X, y):
        predictions = self.predict(X)
        if self.problem_type == 'classification':
            y_ = np.where(y <= 0, -1, 1)
            return np.mean(predictions == y_)
        else:
            ss_tot = np.sum((y - np.mean(y))**2)
            ss_res = np.sum((y - predictions)**2)
            return 1 - (ss_res / ss_tot)
    
    def visualize(self, X, y, title="SVM Decision Boundary"):
        """
        Visualize the decision boundary (classification) or regression line
        Only works for 2D data
        """
        if X.shape[1] != 2:
            print("Visualization only works for 2D data")
            return
            
        fig, ax = plt.subplots(figsize=(10, 8))
        
        if self.problem_type == 'classification':
            # Plot data points
            scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
            
            # Create grid to evaluate model
            x_range = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
            y_range = np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 100)
            xx, yy = np.meshgrid(x_range, y_range)
            grid = np.c_[xx.ravel(), yy.ravel()]
            
            # Calculate decision boundary and margins
            Z = self.predict(grid)
            Z = Z.reshape(xx.shape)
            
            # Plot decision boundary and margins
            ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
                      linestyles=['--', '-', '--'])
            
            ax.set_title(f"Classification: {title}")
            plt.colorbar(scatter)
            
        else:  # regression
            # For regression, we'll plot first feature vs target
            ax.scatter(X[:, 0], y, c='blue', alpha=0.5, label='Data points')
            
            # Plot regression line
            x_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
            X_line = np.c_[x_range, np.mean(X[:, 1]) * np.ones_like(x_range)]
            y_pred = self.predict(X_line)
            
            ax.plot(x_range, y_pred, 'r-', label='Regression line')
            ax.set_title(f"Regression: {title}")
            ax.legend()
        
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2' if self.problem_type == 'classification' else 'Target')
        plt.grid(True)
        plt.show()

# Example usage with visualization
if __name__ == "__main__":
    from sklearn.datasets import make_classification, make_regression
    from sklearn.model_selection import train_test_split
    
    # Classification example
    X_clf, y_clf = make_classification(n_samples=100, n_features=2, n_classes=2, 
                                     n_redundant=0, random_state=42)
    X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
        X_clf, y_clf, test_size=0.2, random_state=42)
    
    svm_clf = SVM(learning_rate=0.001, lambda_param=0.01, n_iterations=1000, 
                 problem_type='classification')
    svm_clf.fit(X_train_clf, y_train_clf)
    print("Classification Accuracy:", svm_clf.score(X_test_clf, y_test_clf))
    svm_clf.visualize(X_clf, y_clf, "SVM Classification Example")
    
    # Regression example
    X_reg, y_reg = make_regression(n_samples=100, n_features=2, noise=10, random_state=42)
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        X_reg, y_reg, test_size=0.2, random_state=42)
    
    svm_reg = SVM(learning_rate=0.001, lambda_param=0.01, n_iterations=1000, 
                 problem_type='regression')
    svm_reg.fit(X_train_reg, y_train_reg)
    print("Regression R2 Score:", svm_reg.score(X_test_reg, y_test_reg))
    svm_reg.visualize(X_reg, y_reg, "SVM Regression Example")