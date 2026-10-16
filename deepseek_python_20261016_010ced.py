# A simple AI model to predict cabin prices
# Based on the coefficients learned in the Elements of AI course

def predict_cabin_price(size, sauna_size, distance_to_lake, toilets, distance_to_neighbor):
    # Coefficients from the course exercise
    c = [3000, 200, -50, 5000, 100]
    
    # Calculate the prediction
    prediction = c[0]*size + c[1]*sauna_size + c[2]*distance_to_lake + c[3]*toilets + c[4]*distance_to_neighbor
    return prediction

# Input values for a new cabin
new_cabin = {
    "Size": 85,
    "Sauna size": 10,
    "Distance to lake": 15,
    "Toilets": 1,
    "Distance to neighbor": 100
}

# Predict the price
price = predict_cabin_price(
    new_cabin["Size"],
    new_cabin["Sauna size"],
    new_cabin["Distance to lake"],
    new_cabin["Toilets"],
    new_cabin["Distance to neighbor"]
)

# Print the result
print(f"Based on the details provided, the predicted price of the cabin is: {price} EUR")