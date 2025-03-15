import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

class KNN:
    def __init__(self, k=3, problem_type='classification'):
        """
        Initialize kNN model parameters
        
        Parameters:
        - k: int, number of nearest neighbors to consider
        - problem_type: str, 'classification' or 'regression'
        """
        self.k = k
        self.problem_type = problem_type
        self.X_train = None
        self.y_train = None
        
    def fit(self, X, y):
        """
        Store training data
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features)
        - y: numpy array of shape (n_samples,)
        """
        self.X_train = X
        self.y_train = y
    
    def _euclidean_distance(self, x1, x2):
        """Calculate Euclidean distance between two points"""
        return np.sqrt(np.sum((x1 - x2) ** 2))
    
    def predict(self, X):
        """
        Make predictions on new data
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features)
        
        Returns:
        - predictions: numpy array of shape (n_samples,)
        """
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)
    
    def _predict(self, x):
        """Make prediction for a single sample"""
        # Compute distances between x and all training samples
        distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]
        
        # Get k nearest samples indices
        k_indices = np.argsort(distances)[:self.k]
        
        # Get k nearest labels/values
        k_nearest = self.y_train[k_indices]
        
        if self.problem_type == 'classification':
            # Return most common class
            most_common = Counter(k_nearest).most_common(1)
            return most_common[0][0]
        else:
            # Return mean of k nearest values
            return np.mean(k_nearest)
    
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
            return np.mean(predictions == y)
        else:
            # R2 score for regression
            ss_tot = np.sum((y - np.mean(y))**2)
            ss_res = np.sum((y - predictions)**2)
            return 1 - (ss_res / ss_tot)
    
    def visualize(self, X, y, title="kNN Decision Boundary"):
        """
        Visualize the decision boundary (classification) or regression surface
        Only works for 2D data
        """
        if X.shape[1] != 2:
            print("Visualization only works for 2D data")
            return
            
        fig, ax = plt.subplots(figsize=(10, 8))
        
        if self.problem_type == 'classification':
            # Plot training points
            scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
            
            # Create grid to evaluate model
            x_range = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
            y_range = np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 100)
            xx, yy = np.meshgrid(x_range, y_range)
            grid = np.c_[xx.ravel(), yy.ravel()]
            
            # Predict for each point in grid
            Z = self.predict(grid)
            Z = Z.reshape(xx.shape)
            
            # Plot decision boundary
            ax.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
            ax.set_title(f"Classification (k={self.k}): {title}")
            plt.colorbar(scatter)
            
        else:  # regression
            # Plot data points
            scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', alpha=0.7)
            
            # For regression with 2 features, we'll plot first feature vs target
            x_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
            X_line = np.c_[x_range, np.mean(X[:, 1]) * np.ones_like(x_range)]
            y_pred = self.predict(X_line)
            
            ax2 = ax.twinx()
            ax2.plot(x_range, y_pred, 'r-', label=f'kNN (k={self.k}) prediction')
            ax2.set_ylabel('Predicted Value')
            ax2.legend()
            
            ax.set_title(f"Regression (k={self.k}): {title}")
            plt.colorbar(scatter, label='Target Value')
        
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
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
    
    knn_clf = KNN(k=5, problem_type='classification')
    knn_clf.fit(X_train_clf, y_train_clf)
    print("Classification Accuracy:", knn_clf.score(X_test_clf, y_test_clf))
    knn_clf.visualize(X_clf, y_clf, "kNN Classification Example")
    
    # Regression example
    X_reg, y_reg = make_regression(n_samples=100, n_features=2, noise=10, random_state=42)
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        X_reg, y_reg, test_size=0.2, random_state=42)
    
    knn_reg = KNN(k=5, problem_type='regression')
    knn_reg.fit(X_train_reg, y_train_reg)
    print("Regression R2 Score:", knn_reg.score(X_test_reg, y_test_reg))
    knn_reg.visualize(X_reg, y_reg, "kNN Regression Example")