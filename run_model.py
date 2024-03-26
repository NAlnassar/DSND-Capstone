import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('bitcoin_price_prediction.h5')

# Predict the price
price = model.predict([[0.5, 0.5, 0.5, 0.5, 0.5]])

# Print the predicted price
print(price)
