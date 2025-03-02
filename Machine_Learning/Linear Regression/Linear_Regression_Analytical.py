import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionAnalytical:
    def __init__(self):
        """Initialize the model."""
        self.slope = None  # B1 (coefficient)
        self.intercept = None  # B0 (intercept)

    def fit(self, X, y):
        """Calculate slope and intercept using the analytical solution."""
        # Calculate means
        x_mean = np.mean(X)
        y_mean = np.mean(y)
        
        # Calculate slope (B1)
        numerator = np.sum((X - x_mean) * (y - y_mean))  # Covariance-like term
        denominator = np.sum((X - x_mean) ** 2)          # Variance of X
        self.slope = numerator / denominator
        
        # Calculate intercept (B0)
        self.intercept = y_mean - self.slope * x_mean
        
        print(f"Calculated slope (B1): {self.slope:.4f}")
        print(f"Calculated intercept (B0): {self.intercept:.4f}")
        return self
    
    def predict(self, X):
        """Predict y using the calculated slope and intercept."""
        return self.slope * X + self.intercept

# Test with raw data
if __name__ == "__main__":
    # Raw data (X: hours studied, y: exam scores)
    np.random.seed(42)
    X = np.linspace(0, 10, 100)  # 100 points from 0 to 10
    y = 2.5 * X + 3 + np.random.normal(0, 2, 100)
    
    # Train the model
    model = LinearRegressionAnalytical()
    model.fit(X, y)
    
    # Predict
    y_pred = model.predict(X)
    
    # Visualize
    plt.scatter(X, y, color='blue', label='Raw data (hours vs. scores)')
    plt.plot(X, y_pred, color='red', label=f'Fitted line: y = {model.slope:.2f}x + {model.intercept:.2f}')
    plt.xlabel('Hours Studied (X)')
    plt.ylabel('Exam Score (y)')
    plt.legend()
    plt.title('Linear Regression: Analytical Solution')
    plt.show()