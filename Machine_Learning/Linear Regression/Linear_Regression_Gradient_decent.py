import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        """Initialize the model with hyperparameters."""
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None  # Slope (coefficient)
        self.bias = None     # Intercept
        self.cost_history = []

    def fit(self, X, y):
        """Train the model to calculate slope (w) and intercept (b)."""
        m = len(X)  # Number of data points
        
        # Initialize slope (w) and intercept (b) to 0
        self.weights = 0
        self.bias = 0
        
        print(f"Initial slope (w): {self.weights}, Initial intercept (b): {self.bias}")
        
        # Gradient descent loop
        for iteration in range(self.n_iterations):
            # Step 1: Compute predictions
            y_pred = self.weights * X + self.bias
            
            # Step 2: Compute gradients
            # Gradient for slope (w): How much the error changes with w
            dw = (1/m) * np.sum((y_pred - y) * X)
            # Gradient for intercept (b): How much the error changes with b
            db = (1/m) * np.sum(y_pred - y)
            
            # Step 3: Update slope and intercept
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Step 4: Compute cost (MSE) to monitor progress
            cost = (1/(2*m)) * np.sum((y_pred - y) ** 2)
            self.cost_history.append(cost)
            
            # Print progress every 100 iterations
            if iteration % 100 == 0:
                print(f"Iteration {iteration}: Slope (w) = {self.weights:.4f}, "
                      f"Intercept (b) = {self.bias:.4f}, Cost = {cost:.4f}")
        
        print(f"Final slope (w): {self.weights:.4f}, Final intercept (b): {self.bias:.4f}")
        return self
    
    def predict(self, X):
        """Predict y using the learned slope and intercept."""
        return self.weights * X + self.bias

# Test with synthetic data (no pre-assumed equation)
if __name__ == "__main__":
    # Generate synthetic data (X and y with a rough linear relationship)
    np.random.seed(42)
    X = np.linspace(0, 10, 100)  # 100 points from 0 to 10
    y = 2.5 * X + 3 + np.random.normal(0, 2, 100)  # Rough linear trend + noise
    
    # Train the model
    model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)
    
    # Visualize the results
    plt.scatter(X, y, color='blue', label='Data points')
    plt.plot(X, y_pred, color='red', label=f'Fitted line: y = {model.weights:.2f}x + {model.bias:.2f}')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.title('Linear Regression: Learning Slope and Intercept')
    plt.show()
    
    # Plot cost history
    plt.plot(model.cost_history)
    plt.xlabel('Iteration')
    plt.ylabel('Cost (MSE)')
    plt.title('Cost History During Training')
    plt.show()