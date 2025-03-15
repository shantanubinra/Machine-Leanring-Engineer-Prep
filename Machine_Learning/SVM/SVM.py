import numpy as np

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iterations=1000, problem_type='classification'):
        """
        Initialize SVM model parameters
        
        Parameters:
        - learning_rate: float, learning rate for gradient descent
        - lambda_param: float, regularization parameter
        - n_iterations: int, number of iterations for optimization
        - problem_type: str, 'classification' or 'regression'
        """
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iterations
        self.problem_type = problem_type
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        """
        Fit the SVM model to the training data
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features)
        - y: numpy array of shape (n_samples,)
        """
        n_samples, n_features = X.shape
        
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Convert y to {-1, 1} for classification
        if self.problem_type == 'classification':
            y_ = np.where(y <= 0, -1, 1)
        else:
            y_ = y
        
        # Gradient Descent optimization
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                if self.problem_type == 'classification':
                    condition = y_[idx] * (np.dot(x_i, self.weights) + self.bias) >= 1
                    
                    if condition:
                        # Update weights with regularization term only
                        dw = 2 * self.lambda_param * self.weights
                        db = 0
                    else:
                        # Update weights with regularization and margin term
                        dw = 2 * self.lambda_param * self.weights - np.dot(x_i, y_[idx])
                        db = -y_[idx]
                    
                else:  # regression
                    # For SVR, use epsilon-insensitive loss
                    epsilon = 0.1
                    prediction = np.dot(x_i, self.weights) + self.bias
                    error = prediction - y_[idx]
                    
                    if abs(error) <= epsilon:
                        dw = 2 * self.lambda_param * self.weights
                        db = 0
                    else:
                        dw = 2 * self.lambda_param * self.weights + x_i * np.sign(error)
                        db = np.sign(error)
                
                # Update parameters
                self.weights -= self.lr * dw
                self.bias -= self.lr * db
    
    def predict(self, X):
        """
        Make predictions on new data
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features)
        
        Returns:
        - predictions: numpy array of shape (n_samples,)
        """
        output = np.dot(X, self.weights) + self.bias
        
        if self.problem_type == 'classification':
            return np.sign(output)
        return output
    
    def score(self, X, y):
        """
        Calculate accuracy for classification or R2 score for regression
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features)
        - y: numpy array of shape (n_samples,)
        
        Returns:
        - score: float
        """
        predictions = self.predict(X)
        
        if self.problem_type == 'classification':
            y_ = np.where(y <= 0, -1, 1)
            return np.mean(predictions == y_)
        else:
            # R2 score for regression
            ss_tot = np.sum((y - np.mean(y))**2)
            ss_res = np.sum((y - predictions)**2)
            return 1 - (ss_res / ss_tot)

# Example usage
if __name__ == "__main__":
    # For classification
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    
    # Generate sample classification data
    # X, y = make_classification(n_samples=100, n_features=2, n_classes=2,  random_state=42)
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, 
                          n_clusters_per_class=1, random_state=42)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Classification example
    svm_clf = SVM(learning_rate=0.001, lambda_param=0.01, n_iterations=1000, 
                 problem_type='classification')
    svm_clf.fit(X_train, y_train)
    print("Classification Accuracy:", svm_clf.score(X_test, y_test))
    
    # For regression
    from sklearn.datasets import make_regression
    
    # Generate sample regression data
    X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Regression example
    svm_reg = SVM(learning_rate=0.001, lambda_param=0.01, n_iterations=1000, 
                 problem_type='regression')
    svm_reg.fit(X_train, y_train)
    print("Regression R2 Score:", svm_reg.score(X_test, y_test))