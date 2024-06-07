import numpy as np

def calculate_errors(y_given, y_pred):
    
    y_given = np.array(y_given)
    y_pred = np.array(y_pred)
    
    # Mean Squared Error (MSE)
    mse = np.mean((y_given - y_pred) ** 2)
    
    # Mean Absolute Error (MAE)
    mae = np.mean(np.abs(y_given - y_pred))
    
    # Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mse)
    
    return {
        "MSE": mse,
        "MAE": mae,
        "RMSE": rmse
    }

# Example usage
y_given = [1, 2, 3, 4, 5]
y_pred = [1.1, 1.9, 3.2, 3.8, 5.3]

errors = calculate_errors(y_given, y_pred)
print("Errors:", errors)
