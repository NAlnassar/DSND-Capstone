# Bitcoin Price Prediction with LSTM

## Libraries Used
- TensorFlow
- NumPy
- Pandas

## Motivation Behind Project
Bitcoin, as a popular cryptocurrency, exhibits highly volatile price behavior, making it an interesting domain for time series forecasting. This project aims to predict Bitcoin prices using Long Short-Term Memory (LSTM) networks. By leveraging deep learning techniques, we seek to develop a model capable of accurately forecasting Bitcoin prices based on historical data.

## Files in the Repository


### 1. `BitcoinPred.ipynb`
- Description: Jupyter Notebook containing Python code for preprocessing the data and training the LSTM model.
- Usage: This notebook guides through loading and preprocessing the Bitcoin price data, defining the LSTM model architecture, training the model, and evaluating its performance.

### 2. `run_model.py`
- Description: Python script to run the trained LSTM model.
- Usage: This script loads the pre-trained model stored in `bitcoin_price_prediction.h5`, accepts user input for predicting Bitcoin prices for a specified date range, and generates predictions.

### 3. `bitcoin_price_prediction.h5`
- Description: HDF5 file containing the trained LSTM model's architecture and weights.
- Usage: This file is used by `run_model.py` to load the trained model for making predictions.

### 4. `Capstone_DS_Report.pdf`
- Description: PDF document providing detailed information about the project, including problem statement, data preprocessing steps, model architecture, training process, evaluation metrics, and conclusions.

## Summary of Results and Analysis
The LSTM model demonstrated promising results in predicting Bitcoin prices. By analyzing the model's performance metrics and visualizing its predictions against actual price data, we observed significant accuracy in forecasting Bitcoin prices over different time periods.

## Conclusion
In conclusion, this project showcases the effectiveness of LSTM networks in Bitcoin price prediction tasks. Through thorough data preprocessing, model training, and evaluation, we successfully developed a robust model capable of capturing complex price patterns and making accurate predictions. The insights gained from this project can be valuable for investors and traders seeking to make informed decisions in the cryptocurrency market.
